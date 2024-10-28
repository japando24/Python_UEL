import json

from PyQt6.QtWidgets import QMessageBox

from Bai134.MainWindow import Ui_MainWindow
class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.msgBox = None
        self.pushButton.clicked.connect(self.getInformation)
    def getInformation(self):
        fullname = self.lineEditFullName.text()
        email = self.lineEditEmail.text()
        gender = "Woman"
        if not self.radioButtonWoman.isChecked():
            gender = self.radioButtonMan.text()
        address = self.lineEditAddress.text()
        degree = "Bachelor"
        if self.radioButtonMaster.isChecked():
            degree = self.radioButtonMaster.text()
        elif self.radioButtonDotocral.isChecked():
            degree = self.radioButtonDotocral.text()
        information = {"FullName": fullname, "Email": email, "Gender": gender, "Address": address, "Degree": degree}
        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle("Information")
        self.msgBox.setText(json.dump(information, ensure_ascii=False))
        self.msgBox.show()
    def show(self):
        self.MainWindow.show()