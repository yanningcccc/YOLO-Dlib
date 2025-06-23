# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 627)

        # 设置窗口背景为渐变色
        MainWindow.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #1E1E2E, stop:1 #282A36);
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 创建主布局，设置上下左右 20px 的空白
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)  # 上下左右留 20px 空白
        self.main_layout.setSpacing(20)  # 各模块之间的间距

        # 标题
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("人脸识别系统")
        self.label.setStyleSheet(
            """
            QLabel {
                color: #F8F8F2;
                font-size: 36px;
                font-family: '微软雅黑';
                font-weight: bold;
                border-bottom: 2px solid #6272A4;
                padding-bottom: 10px;
            }
            """
        )
        self.label.setObjectName("label")
        self.main_layout.addWidget(self.label)  # 将标题添加到主布局

        # 图像显示区域
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setStyleSheet(
            """
            QGraphicsView {
                border: 2px solid #44475A;
                border-radius: 15px;
                background-color: #1E1E2E;
                color: #FFFFFF;
            }
            """
        )
        self.graphicsView.setObjectName("graphicsView")
        self.main_layout.addWidget(self.graphicsView)  # 将图像显示区域添加到主布局

        # 按钮布局
        self.button_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.button_layout_widget.setObjectName("button_layout_widget")

        self.button_layout = QtWidgets.QHBoxLayout(self.button_layout_widget)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(20)

        # 按钮通用样式
        button_style = """
            QPushButton {
                background-color: #44475A;
                color: #F8F8F2;
                font-size: 18px;
                font-family: '微软雅黑';
                font-weight: bold;
                border: 2px solid #6272A4;
                border-radius: 15px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #6272A4;
                color: #FFFFFF;
            }
            QPushButton:pressed {
                background-color: #50FA7B;
                border-color: #50FA7B;
            }
        """

        # 按钮 - 连接摄像头
        self.pushButton = QtWidgets.QPushButton(self.button_layout_widget)
        self.pushButton.setText("连接摄像头")
        self.pushButton.setStyleSheet(button_style)
        self.pushButton.setObjectName("pushButton")
        self.button_layout.addWidget(self.pushButton)

        # 按钮 - 本地加载
        self.pushButton_4 = QtWidgets.QPushButton(self.button_layout_widget)
        self.pushButton_4.setText("本地加载")
        self.pushButton_4.setStyleSheet(button_style)
        self.pushButton_4.setObjectName("pushButton_4")
        self.button_layout.addWidget(self.pushButton_4)

        # 按钮 - 开始检测
        self.pushButton_2 = QtWidgets.QPushButton(self.button_layout_widget)
        self.pushButton_2.setText("开始检测")
        self.pushButton_2.setStyleSheet(button_style)
        self.pushButton_2.setObjectName("pushButton_2")
        self.button_layout.addWidget(self.pushButton_2)

        # 按钮 - 停止
        self.pushButton_3 = QtWidgets.QPushButton(self.button_layout_widget)
        self.pushButton_3.setText("停止")
        self.pushButton_3.setStyleSheet(button_style)
        self.pushButton_3.setObjectName("pushButton_3")
        self.button_layout.addWidget(self.pushButton_3)

        # 将按钮布局添加到主布局
        self.main_layout.addWidget(self.button_layout_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        # 状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 22))
        self.menubar.setStyleSheet("""
            QMenuBar {
                background-color: #1E1E2E;
                color: #F8F8F2;
                font-size: 14px;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 5px 10px;
            }
            QMenuBar::item:selected {
                background-color: #6272A4;
            }
        """)
        self.menubar.setObjectName("menubar")

        # 菜单项
        self.menu111 = QtWidgets.QMenu(self.menubar)
        self.menu111.setObjectName("menu111")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")

        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu111.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸匹配系统"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
