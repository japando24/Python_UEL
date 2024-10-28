from middle_margin import Ui_MainWindow3
class MyMainWindowExt(Ui_MainWindow3):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def show(self):
        self.MainWindow.show()