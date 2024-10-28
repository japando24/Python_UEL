from PyQt6.QtWidgets import QMessageBox, QMainWindow
from Bai118119.InheritenceSignalSlots import Ui_MainWindow
from Bai118119.SecondWindow import SecondWindow


class MyQMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.secondWindow = None
    def processSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonVisitBlog.clicked.connect(self.openMyBlog)
        self.pushButtonSendName.clicked.connect(self.openSecondWindow)
    def processExit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Exit confirmation")
        dlg.setText("Are you sure you want to Exit ?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass
    def show(self):
        self.MainWindow.show()
    def openMyBlog(self):
        import webbrowser
        webbrowser.open("https://store-car-phi.vercel.app/?fbclid=IwY2xjawGLABVleHRuA2FlbQIxMAABHeXfLoEpIg3Nr1l8ZDmk-VQRH86lJKihOhrWnTJH8CXdF46GaY9P7EPY8Q_aem_V8llvyIm8NO_gQwj-7GIYA")
    def openSecondWindow(self):
        if self.secondWindow == None or self.qmainWindow.isVisible() == False:
            self.qmainWindow = QMainWindow()
            self.secondWindow = SecondWindow (self)
            self.secondWindow.setupUi(self.qmainWindow)
            self.qmainWindow.show()
    def changeRedColor(self):
        self.MainWindow.setStyleSheet("background-color: red;")
    def changeYellowColor(self):
        self.MainWindow.setStyleSheet("background-color: yellow")
