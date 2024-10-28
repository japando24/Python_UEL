from PyQt6.QtWidgets import QApplication, QMainWindow

from SignalandSlotsMainWindowEx import SignalandSlotsMainWindowEx

app = QApplication([])
myWindow = SignalandSlotsMainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()