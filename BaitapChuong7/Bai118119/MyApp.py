from PyQt6.QtWidgets import QApplication, QMainWindow
from Bai118119.InheritenceSignalSlotsExt import MyQMainWindowExt
app = QApplication([])
myWindow = MyQMainWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.processSignalAndSlot()
myWindow.show()
app.exec()