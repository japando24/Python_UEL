from Bai127.MainWindow import Ui_MainWindow
class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonConvert.clicked.connect(self.convert)
    def show(self):
        self.MainWindow.show()
    def convert(self):
        f = float(self.lineEditFahrenheit.text())
        result = (f - 32)*5/9
        result = round(result, 2)
        self.labelDisplayResult.setText(str(result))
