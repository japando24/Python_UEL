from MainWindow import Ui_MainWindow
class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        # change text
        self.pushButtonChangeText.clicked.connect(self.processChangeText)
    def show(self):
        self.MainWindow.show()
    def processChangeText(self):
        self.labelTitle.setText("Nguyen Bao Huy")

