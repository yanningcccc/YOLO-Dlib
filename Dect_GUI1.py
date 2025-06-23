import cv2
import sqlite3
import torch
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtWidgets import QGraphicsScene, QMessageBox,QFileDialog
from ultralytics import YOLO
import numpy as np
import os

import dlib
from Dect_GUI2 import Ui_MainWindow

class Dect_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Dect_MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initConnections()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.cap = None
        self.cap2 = None
        self.cap3 = None
        self.choice = 0
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.model = YOLO('face.pt')
        self.detector = dlib.get_frontal_face_detector()
        self.sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
        self.class_names = ['face']
        self.conn = sqlite3.connect('./数据库/ceshi.db')
    def initConnections(self):  # 连接按钮信号与槽函数
        self.ui.pushButton.clicked.connect(self.StartCamera)  # 连接摄像头
        self.ui.pushButton_2.clicked.connect(self.StartDetect)  # 读取视频数据，并调用已经训练好的模型进行实时检测
        self.ui.pushButton_3.clicked.connect(self.Stopanalysis)  # 停止
        self.ui.pushButton_4.clicked.connect(self.Dataload)

    def StartCamera(self):
        self.choice = 1
        if self.cap is None:  # 如果摄像头未初始化，则初始化
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():  # 检查摄像头是否成功打开
                QMessageBox.critical(self, "摄像头错误", "无法打开摄像头，请确保摄像头已连接正确并且没有其他应用正在使用它。")
                return
            self.timer.timeout.connect(self.update_frame)  # 连接定时器到显示视频流的方法
            self.timer.start(30)  # 以30ms的间隔定时更新帧

    def update_frame(self):
        if self.cap is not None:
            ret, frame = self.cap.read()  # 读取一帧
        elif self.cap2 is not None:
            ret,frame = self.cap2.read()
        elif self.cap3 is not None:
            frame = self.cap3
            ret = True
        if ret:
            image = self.convert_cv_qt(frame)  # 将cv2图像转换为QImage
            self.scene.clear()  # 清除场景
            self.scene.addPixmap(QPixmap.fromImage(image))  # 将转换后的图像添加到场景

    def convert_cv_qt(self, cv_img):
        """将cv2图像转换为QImage"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(551, 361, QtCore.Qt.KeepAspectRatio)
        return p
    def StartDetect(self):
        print("StartDetect called")  # 确认方法被调用
        if self.choice == 1:
            if self.cap is None:  # 如果摄像头未初始化，则初始化
                print("Initializing camera")  # 添加打印语句
                self.StartCamera()
            if self.cap.isOpened():  # 确保摄像头已经打开
                print("Camera is opened")  # 添加打印语句
                if self.timer.isActive():  # 检查定时器是否已经在运行
                    print("Timer is already active, reconnecting to update_detection")  # 添加打印语句
                    self.timer.timeout.disconnect(self.update_frame)  # 断开显示视频流的方法
                    self.timer.timeout.connect(self.update_detection)  # 重新连接定时器到检测方法
                else:
                    print("Timer is not active, starting timer")  # 添加打印语句
                    self.timer.timeout.connect(self.update_detection)  # 连接定时器到检测方法
                    self.timer.start(30)  # 启动定时器以每30ms进行一次检测
                print("Timer should now be connected to update_detection")  # 添加打印语句
            else:
                QMessageBox.critical(self, "摄像头错误", "摄像头未成功打开。")
        elif self.choice == 2:
            ret, frame = self.cap2.read()
            if ret is False:
                print('视频未加载成功')
            else:
                if self.timer.isActive():  # 检查定时器是否已经在运行
                    print("Timer is already active, reconnecting to update_detection")  # 添加打印语句
                    self.timer.timeout.disconnect(self.update_frame)  # 断开显示视频流的方法
                    self.timer.timeout.connect(self.update_detection)  # 重新连接定时器到检测方法
                else:
                    print("Timer is not active, starting timer")  # 添加打印语句
                    self.timer.timeout.connect(self.update_detection)  # 连接定时器到检测方法
                    self.timer.start(30)  # 启动定时器以每30ms进行一次检测
                print("Timer should now be connected to update_detection")  # 添加打印语句
        elif self.choice == 3:
            frame = self.cap3
            if frame is None:
                print("图像未加载或无效，请检查图像路径。")
            print("图像加载成功，开始检测...")

            self.update_detection()  # 调用图像检测方法

    def update_detection(self):
        print("update_detection called")  # 添加打印语句
        if self.cap is not None:
            ret, frame = self.cap.read()  # 读取一帧，frame则为1帧对应的图像数据
        elif self.cap2 is not None:
            ret,frame = self.cap2.read()
        elif self.cap3 is not None:
            frame = self.cap3
            ret = True
        if ret:
            detections = self.detect_objects(frame)  # 调用目标检测函数

            if not detections:
                self.display_detections(frame,[])
                return
            x1,y1,x2,y2,conf = detections[0]
            face_roi = frame[y1:y2, x1:x2]
            if face_roi.size == 0:
                self.display_detections(frame,[])
                return

            image_name,faces = self.face_matching(frame)
            self.display(frame,image_name,faces,detections)

    def face_matching(self,frame):
        cursor=self.conn.cursor()
        cursor.execute("SELECT id,name,type,data FROM Image")
        results = cursor.fetchall()
        feat1,faces = self.extract_face_feature(frame)
        if(faces == 0):
            return  0,0
        for row in results:
            image_name = row[1]
            image_type = row[2]
            image_data = row[3]

            nparr = np.frombuffer(image_data,np.uint8)
            img = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
            feat2,faces = self.extract_face_feature(img)

            distance = np.linalg.norm(feat1 - feat2)
            threshold = 0.5
            if distance < threshold:
                return image_name,faces
        image_name = 0
        return image_name,faces

    def display(self,frame,image_name,faces,detections):
        if(faces==0):
            height, width = frame.shape[:2]
            label = "Face NOT Find "
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            thickness = 2
            (text_width, text_height), baseline = cv2.getTextSize(label, font, font_scale, thickness)

            # 计算居中坐标
            center_x = width // 2 - text_width // 2
            center_y = height // 2 + text_height // 2

            # 绘制文本（居中显示）
            cv2.putText(frame, label, (center_x, center_y), font, font_scale, (0, 255, 0), thickness)
            image = self.convert_cv_qt(frame)  # 将cv2图像转换为QImage
            self.scene.clear()  # 清除场景
            self.scene.addPixmap(QPixmap.fromImage(image))  # 将转换后的图像添加到场景

            return 0

        x1, y1, x2, y2, conf = detections[0]
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

        if(image_name != 0):
            label = f"Welcome {image_name}"
        else:
            label = "Matching fail"

        cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        image = self.convert_cv_qt(frame)  # 将cv2图像转换为QImage
        self.scene.clear()  # 清除场景
        self.scene.addPixmap(QPixmap.fromImage(image))  # 将转换后的图像添加到场景
        return 0

    def extract_face_feature(self,frame):
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        if not faces:
            return 0,0
        shape = self.sp(gray,faces[0])
        descriptor = self.facerec.compute_face_descriptor(frame,shape)
        return np.array(descriptor),faces

    def Stopanalysis(self):
        if self.cap:
            self.cap.release()  # 释放摄像头资源
            self.cap = None
            self.timer.stop()  # 停止定时器
            self.scene.clear()  # 清除场景
        if self.cap2:
            self.cap2.release()  # 释放摄像头资源
            self.cap2 = None
            self.timer.stop()  # 停止定时器
            self.scene.clear()  # 清除场景
        if self.cap3 is not None:
            self.cap3 = None
            self.scene.clear()  # 清除场景

        # 功能：加载本地视频进行检测
    def Dataload(self):

        # 打开文件对话框，允许用户选择图片或视频文件
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(None, "选择图片或视频", "",
                                                "所有文件 (*);;图片文件 (*.jpg *.png *.bmp);;视频文件 (*.mp4 *.avi)",
                                                options=options)
        if not file:  # 如果没有选择文件，返回
            return
        file_extension = os.path.splitext(file)[1].lower()
        if file_extension in ['.jpg', '.png', '.bmp']:
            self.choice = 3
            self.cap3 = cv2.imread(file)
            self.update_frame()
        # 如果是视频文件
        elif file_extension in ['.mp4', '.avi']:
            self.choice = 2
            self.cap2 = cv2.VideoCapture(file)  # 打开视频文件

            if not self.cap2.isOpened():  # 检查视频是否打开成功
                print("无法打开视频文件")
                return
            self.timer.timeout.connect(self.update_frame)  # 连接定时器到显示视频流的方法
            self.timer.start(300)  # 以30ms的间隔定时更新帧
    def detect_objects(self, frame):
        results = self.model.predict(frame)  # 对帧进行预测
        max_conf = 0.0
        for result in results:
            boxes = result.boxes  # 使用 result.boxes 获取边界框信息
            if boxes is not None:
                for box in boxes:
                    xyxy_data = box.xyxy[0].cpu().numpy()  # 转换为 numpy 数组
                    x1, y1, x2, y2 = xyxy_data.astype(int)  # 确保坐标值是整数类型
                    conf = box.conf[0].item()
                    if conf > max_conf:
                        max_conf = conf
                        best_detection = (x1, y1, x2, y2, conf)
        return [best_detection] if best_detection else []  # 返回检测结果
    def display_detections(self, frame, detections):
        for detection in detections:
            x1, y1, x2, y2, confidence, class_id = detection
            print(f"Detection: ({x1}, {y1}), ({x2}, {y2}) - Confidence: {confidence}, Class: {class_id}")
            x1, y1, x2, y2 = max(0, int(x1)), max(0, int(y1)), min(frame.shape[1], int(x2)), min(frame.shape[0],
                                                                                                     int(y2))
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            class_name = self.class_names[int(class_id)]
            label = f"{class_name}: {confidence:.2f}"
            cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        ret, frame = cv2.imencode('.jpg', frame)
        image = self.convert_cv_qt(frame)
        self.scene.clear()
        self.scene.addPixmap(QPixmap.fromImage(image))

