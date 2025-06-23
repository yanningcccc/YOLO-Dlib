# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginGUI2(object):
    def setupUi(self, LoginGUI2):
        LoginGUI2.setObjectName("LoginGUI2")
        LoginGUI2.resize(800, 600)
        LoginGUI2.setStyleSheet("background-color: #2E3440;")  # 背景颜色更现代化
        self.centralwidget = QtWidgets.QWidget(LoginGUI2)
        self.centralwidget.setObjectName("centralwidget")

        # 主布局
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main_layout.setSpacing(20)

        # 标题
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("智能人脸匹配系统")
        self.label.setStyleSheet("color: #88C0D0; font-size: 32px; font-family: '黑体'; font-weight: bold;")
        self.main_layout.addWidget(self.label)

        # 用户名布局
        self.user_layout = QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("用户名：")
        self.label_2.setStyleSheet("color: #ECEFF4; font-size: 18px; font-family: 'Arial'; font-weight: bold;")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setPlaceholderText("请输入用户名")
        self.lineEdit.setStyleSheet(
            "font-size: 16px; padding: 5px; border: 2px solid #4C566A; border-radius: 5px; background-color: #3B4252; color: #ECEFF4;"
        )
        self.user_layout.addWidget(self.label_2)
        self.user_layout.addWidget(self.lineEdit)
        self.main_layout.addLayout(self.user_layout)

        # 密码布局
        self.password_layout = QtWidgets.QHBoxLayout()
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("密    码：")
        self.label_3.setStyleSheet("color: #ECEFF4; font-size: 18px; font-family: 'Arial'; font-weight: bold;")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setPlaceholderText("请输入密码")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setStyleSheet(
            "font-size: 16px; padding: 5px; border: 2px solid #4C566A; border-radius: 5px; background-color: #3B4252; color: #ECEFF4;"
        )
        self.password_layout.addWidget(self.label_3)
        self.password_layout.addWidget(self.lineEdit_2)
        self.main_layout.addLayout(self.password_layout)

        # 按钮布局
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setSpacing(30)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setText("登录")
        self.pushButton.setStyleSheet(
            "font-size: 16px; padding: 10px; border: none; border-radius: 10px; background-color: #5E81AC; color: #ECEFF4;"
        )
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setText("退出")
        self.pushButton_2.setStyleSheet(
            "font-size: 16px; padding: 10px; border: none; border-radius: 10px; background-color: #BF616A; color: #ECEFF4;"
        )
        self.button_layout.addWidget(self.pushButton)
        self.button_layout.addWidget(self.pushButton_2)
        self.main_layout.addLayout(self.button_layout)

        # 管理员登录按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setText("管理员登录")
        self.pushButton_3.setStyleSheet(
            "font-size: 14px; padding: 8px; border: 2px solid #4C566A; border-radius: 10px; background-color: #3B4252; color: #ECEFF4;"
        )
        self.main_layout.addWidget(self.pushButton_3, alignment=QtCore.Qt.AlignLeft)

        LoginGUI2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginGUI2)
        self.statusbar.setObjectName("statusbar")
        LoginGUI2.setStatusBar(self.statusbar)

        self.retranslateUi(LoginGUI2)
        QtCore.QMetaObject.connectSlotsByName(LoginGUI2)

    def retranslateUi(self, LoginGUI2):
        _translate = QtCore.QCoreApplication.translate
        LoginGUI2.setWindowTitle(_translate("LoginGUI2", "智能人脸匹配系统"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginGUI2 = QtWidgets.QMainWindow()
    ui = Ui_LoginGUI2()
    ui.setupUi(LoginGUI2)
    LoginGUI2.show()
    sys.exit(app.exec_())
