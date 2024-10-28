from Bai117.SignalandSlotsMainWindow import Ui_MainWindow
class SignalandSlotsMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonChangeColor.clicked.connect(self.changeBackground)
    def show(self):
        self.MainWindow.show()
    def changeBackground(self):
        self.MainWindow.setStyleSheet("background-color: blue;")