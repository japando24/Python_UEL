from middle2_margin import Ui_MainWindow2
class MyMainWindowExt(Ui_MainWindow2):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def show(self):
        self.MainWindow.show()