from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from LoginDialog import Ui_LoginDialog
from managercontrolUI import Ui_managercontrol
from PyQt5.QtWidgets import QMessageBox
import sys
from managercontrol2 import managercontrol
from managerLogin import Ui_managerLogin

class managerLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(managerLogin, self).__init__()
        self.ui = Ui_managerLogin()
        self.ui.setupUi(self)
        self.ui.logining.clicked.connect(self.checkLogin)
        self.ui.turnback.clicked.connect(self.close)
        self.usernameEdit = self.ui.lineEdit
        self.passwordEdit = self.ui.lineEdit_2

    def checkLogin(self):
        username = self.usernameEdit.text().strip()  # 去除空格并转换为小写
        password = self.passwordEdit.text().strip()  # 去除空格并转换为小写
        if self.validateCredentials(username, password):
            self.openMainWindow()
        else:
            QMessageBox.warning(self, '错误', '用户名或密码错误')

    def validateCredentials(self, username, password):
        try:
            # 连接 SQLite 数据库
            conn = sqlite3.connect('./数据库/ceshi.db')  # 数据库文件路径
            cursor = conn.cursor()

            # 查询用户名和密码
            query = "SELECT 1 FROM manager WHERE username = ? AND password = ?"
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
        self.mainWindow = managercontrol()  # 此处创建实例
        self.mainWindow.show()
        print("Main window shown.")
        self.close()

def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    try:
        login_window = managerLogin()
        login_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)



if __name__ == '__main__':
    main()
