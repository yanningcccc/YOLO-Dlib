from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from LoginDialog import Ui_LoginDialog
from managercontrolUI import Ui_managercontrol
from PyQt5.QtWidgets import QMessageBox
import sys
class managercontrol(QtWidgets.QMainWindow):
    def __init__(self):
        super(managercontrol, self).__init__()
        self.ui = Ui_managercontrol()
        self.ui.setupUi(self)
        self.ui.adduser.clicked.connect(self.adduser)
        self.ui.queryuser.clicked.connect(self.queryuser)
        self.ui.deleteuser.clicked.connect(self.deleteuser)
        self.ui.turnback.clicked.connect(self.close)
    def adduser(self):
        class adduserWnd(QtWidgets.QDialog):
            def __init__(self):
                super(adduserWnd,self).__init__()
                self.ui = Ui_LoginDialog()
                self.ui.setupUi(self)
                self.ui.loginBtn.clicked.connect(self.add)
                self.ui.registerBtn.clicked.connect(self.close)
                self.usernameEdit = self.ui.accountEdit
                self.passwordEdit = self.ui.accountEdit_2
            def add(self):
                """添加用户"""
                username = self.usernameEdit.text()
                password = self.passwordEdit.text()
                try:
                    conn = sqlite3.connect('./数据库/ceshi.db')
                    cursor = conn.cursor()

                    query = "INSERT INTO user (username, password) VALUES (?, ?)"
                    cursor.execute(query, (username, password))
                    conn.commit()

                    QMessageBox.information(self, "成功", "用户添加成功！")
                except sqlite3.IntegrityError:
                    QMessageBox.warning(self, "失败", "用户名已存在！")
                except Exception as e:
                    QMessageBox.critical(self, "错误", f"发生错误: {e}")
                finally:
                    if 'conn' in locals():
                        conn.close()
        self.yes = adduserWnd()
        self.yes.show()
    def queryuser(self):
        class queryuserWnd(QtWidgets.QDialog):
            def __init__(self):
                super(queryuserWnd,self).__init__()
                self.ui = Ui_LoginDialog()
                self.ui.setupUi(self)
                self.ui.loginBtn.clicked.connect(self.query)
                self.ui.registerBtn.clicked.connect(self.close)
                self.usernameEdit = self.ui.accountEdit
                self.passwordEdit = self.ui.accountEdit_2

            def query(self):
                """查询用户"""
                username = self.usernameEdit.text()
                try:
                    conn = sqlite3.connect('./数据库/ceshi.db')
                    cursor = conn.cursor()

                    # 查询用户
                    query = "SELECT * FROM user WHERE username = ?"
                    cursor.execute(query, (username,))
                    result = cursor.fetchone()

                    if result:
                        QMessageBox.information(self, "查询结果", f"用户信息：\n用户名：{result[1]}\n密码：{result[2]}")
                    else:
                        QMessageBox.warning(self, "未找到", "用户不存在！")
                except Exception as e:
                    QMessageBox.critical(self, "错误", f"发生错误: {e}")
                finally:
                    if 'conn' in locals():
                        conn.close()
        self.yes = queryuserWnd()
        self.yes.show()
    def deleteuser(self):
        class deleteuserWnd(QtWidgets.QDialog):
            def __init__(self):
                super(deleteuserWnd,self).__init__()
                self.ui = Ui_LoginDialog()
                self.ui.setupUi(self)
                self.ui.loginBtn.clicked.connect(self.delete)
                self.ui.registerBtn.clicked.connect(self.close)
                self.usernameEdit = self.ui.accountEdit
                self.passwordEdit = self.ui.accountEdit_2
            def delete(self):
                """删除用户"""
                username = self.usernameEdit.text()
                try:
                    conn = sqlite3.connect('./数据库/ceshi.db')
                    cursor = conn.cursor()

                    # 删除用户
                    query = "DELETE FROM user WHERE username = ?"
                    cursor.execute(query, (username,))
                    conn.commit()

                    if cursor.rowcount > 0:
                        QMessageBox.information(self, "成功", "用户删除成功！")
                    else:
                        QMessageBox.warning(self, "失败", "用户不存在，无法删除！")
                except Exception as e:
                    QMessageBox.critical(self, "错误", f"发生错误: {e}")
                finally:
                    if 'conn' in locals():
                        conn.close()
        self.yes = deleteuserWnd()
        self.yes.show()
def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtGui.QGuiApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QtWidgets.QApplication(sys.argv)
    try:
        login_window = managercontrol()
        login_window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()