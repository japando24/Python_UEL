from PyQt6.QtWidgets import QApplication, QMainWindow
from Bai114.HelloWorldMainWindowEx import HelloWorldMainWindowEx
app = QApplication([])
myWindow = HelloWorldMainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()