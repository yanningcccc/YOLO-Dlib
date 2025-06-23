import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Dect_GUI1 import Dect_MainWindow
from Login2 import Ui_LoginGUI2
from managerLogin2 import managerLogin
import sqlite3


class LoginGUI2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoginGUI2, self).__init__(parent)
        self.ui = Ui_LoginGUI2()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.checkLogin)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.manager)
        self.usernameEdit = self.ui.lineEdit
        self.passwordEdit = self.ui.lineEdit_2

    def checkLogin(self):
        username = self.usernameEdit.text().strip()
        password = self.passwordEdit.text().strip()
        if self.validateCredentials(username, password):
            self.openMainWindow()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('错误')
            msg.setText('用户名或密码错误')

            # 设置样式表 - 使文本变为白色
            msg.setStyleSheet("""
                        QMessageBox {
                            background-color: #333;  /* 深色背景使白色文字更醒目 */
                        }
                        QLabel { 
                            color: white;   /* 设置文本颜色为白色 */
                            font-size: 14px;
                        }
                        QPushButton {
                            background-color: #555;
                            color: white;
                            border: 1px solid #888;
                            padding: 5px;
                            min-width: 70px;
                        }
                    """)
            # 添加确定按钮
            msg.addButton(QMessageBox.Ok)
            msg.exec_()
            # QMessageBox.warning(self, '错误', '用户名或密码错误')

    def validateCredentials(self, username, password):
        try:
            # 连接 SQLite 数据库
            conn = sqlite3.connect('./数据库/ceshi.db')  # 数据库文件路径
            cursor = conn.cursor()

            # 查询用户名和密码
            query = "SELECT 1 FROM user WHERE username = ? AND password = ?"
            cursor.execute(query, (username.strip(), password.strip()))
            result = cursor.fetchone()

            # 如果找到匹配记录，返回 True，否则返回 False
            return bool(result)
        except sqlite3.OperationalError as e:
            QMessageBox.critical(self, '数据库错误', f'无法查询数据库: {e}')
            return False
        except Exception as e:
            QMessageBox.critical(self, '错误', f'发生错误: {e}')
            return False
        finally:
            # 确保数据库连接被关闭
            if 'conn' in locals():
                conn.close()

    def openMainWindow(self):
        print("Opening main window...")  # 调试信息
        self.hide()
        self.mainWindow = Dect_MainWindow()  #  此处创建实例
        self.mainWindow.show()
        print("Main window shown.")
        self.close()
    def manager(self):
        self.ui2 = managerLogin()
        self.ui2.show()

# 主函数
def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    try:
        login_window = LoginGUI2()
        login_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()