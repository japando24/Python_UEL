from PyQt6.QtWidgets import QApplication, QMainWindow

from MyMainWindowExt import MyMainWindowExt
app = QApplication([])
myWindow1 = MyMainWindowExt()
myWindow1.setupUi(QMainWindow())
myWindow1.show()
app.exec()

