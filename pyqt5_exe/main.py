import sys
from pyqt5_exe import winmian

from PyQt5.QtWidgets import QApplication, QMainWindow
from winmian import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton1)

    def pushButton1(self):
        self.textBrowser.setText("222222")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
