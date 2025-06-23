# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_managercontrol(object):
    def setupUi(self, managercontrol):
        managercontrol.setObjectName("managercontrol")
        managercontrol.resize(1000, 700)

        # 设置背景为渐变色
        managercontrol.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                                            stop:0 #4C566A, stop:1 #2E3440);
            }
        """)

        self.centralwidget = QtWidgets.QWidget(managercontrol)
        self.centralwidget.setObjectName("centralwidget")

        # 主标题
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 600, 60))
        self.label.setText("管理员操作界面")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: #ECEFF4;
                font-size: 36px;
                font-family: '微软雅黑';
                font-weight: bold;
                border-bottom: 2px solid #88C0D0;
            }
        """)

        # 操作选择标题
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 150, 200, 40))
        self.label_2.setText("请选择操作")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setStyleSheet("""
            QLabel {
                color: #D8DEE9;
                font-size: 24px;
                font-family: '微软雅黑';
                font-weight: bold;
            }
        """)

        # 按钮布局
        self.button_layout = QtWidgets.QGridLayout()
        self.button_layout_widget = QtWidgets.QWidget(self.centralwidget)
        self.button_layout_widget.setGeometry(QtCore.QRect(250, 250, 500, 300))
        self.button_layout_widget.setLayout(self.button_layout)

        # 按钮通用样式
        button_style = """
            QPushButton {
                font-size: 18px;
                font-family: '微软雅黑';
                padding: 10px;
                border-radius: 20px;
                color: #ECEFF4;
                background-color: #5E81AC;
                border: 2px solid #88C0D0;
            }
            QPushButton:hover {
                background-color: #88C0D0;
                color: #2E3440;
            }
            QPushButton:pressed {
                background-color: #4C566A;
                border-color: #81A1C1;
            }
        """

        # 添加用户按钮
        self.adduser = QtWidgets.QPushButton(self.centralwidget)
        self.adduser.setText("添加用户")
        self.adduser.setStyleSheet(button_style)
        self.button_layout.addWidget(self.adduser, 0, 0)

        # 查询用户按钮
        self.queryuser = QtWidgets.QPushButton(self.centralwidget)
        self.queryuser.setText("查询用户")
        self.queryuser.setStyleSheet(button_style)
        self.button_layout.addWidget(self.queryuser, 0, 1)

        # 删除用户按钮
        self.deleteuser = QtWidgets.QPushButton(self.centralwidget)
        self.deleteuser.setText("删除用户")
        self.deleteuser.setStyleSheet(button_style)
        self.button_layout.addWidget(self.deleteuser, 1, 0)

        # 返回按钮
        self.turnback = QtWidgets.QPushButton(self.centralwidget)
        self.turnback.setText("返回")
        self.turnback.setStyleSheet(button_style)
        self.button_layout.addWidget(self.turnback, 1, 1)

        managercontrol.setCentralWidget(self.centralwidget)

        # 状态栏
        self.statusbar = QtWidgets.QStatusBar(managercontrol)
        self.statusbar.setObjectName("statusbar")
        managercontrol.setStatusBar(self.statusbar)

        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(managercontrol)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menu111 = QtWidgets.QMenu(self.menubar)
        self.menu111.setObjectName("menu111")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        managercontrol.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu111.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(managercontrol)
        QtCore.QMetaObject.connectSlotsByName(managercontrol)

    def retranslateUi(self, managercontrol):
        _translate = QtCore.QCoreApplication.translate
        managercontrol.setWindowTitle(_translate("managercontrol", "管理员操作界面"))
        self.menu111.setTitle(_translate("managercontrol", "开始"))
        self.menu.setTitle(_translate("managercontrol", "关于"))
        self.menu_2.setTitle(_translate("managercontrol", "帮助"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    managercontrol = QtWidgets.QMainWindow()
    ui = Ui_managercontrol()
    ui.setupUi(managercontrol)
    managercontrol.show()
    sys.exit(app.exec_())
