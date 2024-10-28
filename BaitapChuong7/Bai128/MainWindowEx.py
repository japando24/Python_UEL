from Bai128.MainWindow import Ui_MainWindow
class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonConvert.clicked.connect(self.convertYear)
    def show(self):
        self.MainWindow.show()
    def convertYear(self):
        year_input = int(self.lineEditFahrenheit.text())
        if year_input < 0:
            self.labelError.setText("You need enter a positive a number")
            return
        result = ""
        can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
        chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

        result = f"{can[year_input%10]} {chi[year_input%12]}"
        self.labelDisplayResult.setText(result)
