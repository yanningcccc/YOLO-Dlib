# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_managerLogin(object):
    def setupUi(self, managerLogin):
        managerLogin.setObjectName("managerLogin")
        managerLogin.resize(800, 600)

        # 设置背景颜色
        managerLogin.setStyleSheet("background-color: #2E3440;")  # 深色背景，更现代化

        self.centralwidget = QtWidgets.QWidget(managerLogin)
        self.centralwidget.setObjectName("centralwidget")

        # 主布局
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main_layout.setSpacing(20)

        # 标题
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("管理员登录界面")
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

        self.logining = QtWidgets.QPushButton(self.centralwidget)
        self.logining.setText("登录")
        self.logining.setStyleSheet(
            "font-size: 16px; padding: 10px; border: none; border-radius: 10px; background-color: #5E81AC; color: #ECEFF4;"
        )
        self.turnback = QtWidgets.QPushButton(self.centralwidget)
        self.turnback.setText("返回")
        self.turnback.setStyleSheet(
            "font-size: 16px; padding: 10px; border: none; border-radius: 10px; background-color: #BF616A; color: #ECEFF4;"
        )
        self.button_layout.addWidget(self.logining)
        self.button_layout.addWidget(self.turnback)
        self.main_layout.addLayout(self.button_layout)

        managerLogin.setCentralWidget(self.centralwidget)

        # 状态栏
        self.statusbar = QtWidgets.QStatusBar(managerLogin)
        self.statusbar.setObjectName("statusbar")
        managerLogin.setStatusBar(self.statusbar)

        self.retranslateUi(managerLogin)
        QtCore.QMetaObject.connectSlotsByName(managerLogin)

    def retranslateUi(self, managerLogin):
        _translate = QtCore.QCoreApplication.translate
        managerLogin.setWindowTitle(_translate("managerLogin", "管理员登录界面"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    managerLogin = QtWidgets.QMainWindow()
    ui = Ui_managerLogin()
    ui.setupUi(managerLogin)
    managerLogin.show()
    sys.exit(app.exec_())
