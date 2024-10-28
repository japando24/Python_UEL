from PyQt6.QtWidgets import QApplication, QMainWindow
from Bai130.MainWindowEx import MainWindowEx
app = QApplication([])
myWindow = MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.processSignalAndSlot()
myWindow.show()
app.exec()