from bottom_margin import Ui_MainWindow1
class MyMainWindowExt(Ui_MainWindow1):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def show(self):
        self.MainWindow.show()