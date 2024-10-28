from PyQt6.QtWidgets import QApplication, QMainWindow

from MyMainWindowExt import MyMainWindowExt
app = QApplication([])
myWindow2 = MyMainWindowExt()
myWindow2.setupUi(QMainWindow())
myWindow2.show()
app.exec()

