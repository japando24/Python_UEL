from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindowDegreeEquationExt import MainWindowFirstDegreeEquation
app = QApplication([])
myWindow = MainWindowFirstDegreeEquation()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()