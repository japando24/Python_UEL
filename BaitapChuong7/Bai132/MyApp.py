from PyQt6.QtWidgets import QMainWindow, QApplication

from Bai132.MainWindowEx import MainWindowEx
app = QApplication([])
myWindow = MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()