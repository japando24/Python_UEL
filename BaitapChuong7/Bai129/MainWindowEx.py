from PyQt6.QtWidgets import QMessageBox
from Bai129.MainWindow import Ui_MainWindow
class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.dlg = None
    def processSignalAndSlot(self):
        self.pushButtonGuide.clicked.connect(self.processGuide)
        self.pushButtonBusiness.clicked.connect(self.processElectricityBusiness)
        self.pushButtonContinue.clicked.connect(self.processContinue)
        self.pushButtonManufacturer.clicked.connect(self.processElectricityManufacturer)
        self.pushButtonSHBT.clicked.connect(self.processElectricitySHBT)
    def processElectricityBusiness(self):
        A = float(self.lineEditOldNumber.text())
        B = float(self.lineEditNewNumber.text())
        if A < 0 or B < 0:
            self.labeError.setText("Số điện phải dương !!!")
            return
        if A > B:
            self.labeError.setText("Số điện cũ phải nhỏ hơn số điện mới !!!")
            return
        self.labeError.setText("")
        money = (B-A)*2320
        result = f"Tiền kinh doanh = {money} (VNĐ)"
        self.labelDisplayMoney.setText(result)
        self.lineEditKWh.setText(str(B-A))
    def processElectricityManufacturer(self):
        A = float(self.lineEditOldNumber.text())
        B = float(self.lineEditNewNumber.text())
        if A < 0 or B < 0:
            self.labeError.setText("Số điện phải dương !!!")
            return
        if A > B:
            self.labeError.setText("Số điện cũ phải bé hơn số điện mới !!!")
            return
        self.labeError.setText("")
        money = (B - A) * 1518
        result = f"Tiền sản xuất = {money} (VNĐ)"
        self.labelDisplayMoney.setText(result)
        self.lineEditKWh.setText(str(B-A))
    def processElectricitySHBT(self):
        A = float(self.lineEditOldNumber.text())
        B = float(self.lineEditNewNumber.text())
        C = float(self.lineEditSHBT.text())
        if A < 0 or B < 0 or C < 0:
            self.labeError.setText("Số điện hay số hộ dùng chung phải dương !!!")
            return
        if A > B:
            self.labeError.setText("Số điện cũ phải lớn hơn số điện mới  !!!")
            return
        self.labeError.setText("")
        dict_rank_elec = {
            "1": 1484,
            "2": 1533,
            "3": 1786,
            "4": 2242,
            "5": 2503,
            "6": 2587,
        }
        result = 0

        match (B - A):
            case x if x <= 50 * C:
                result = (B - A) * dict_rank_elec["1"]
            case x if x <= 100 * C:
                result =  (50 * C * dict_rank_elec["1"]) + ((B - A) - 50 * C) * dict_rank_elec["2"]
            case x if x <= 200 * C:
                result =  (50 * C * dict_rank_elec["1"]) + (50 * C * dict_rank_elec["2"]) + (
                        (B - A) - 100 * C) * dict_rank_elec["3"]
            case x if x <= 300 * C:
                result =  (50 * C * dict_rank_elec["1"]) + (50 * C * dict_rank_elec["2"]) + (
                        100 * C * dict_rank_elec["3"]) + ((B - A) - 200 * C) * dict_rank_elec["4"]
            case x if x <= 400 * C:
                result =  (50 * C * dict_rank_elec["1"]) + (50 * C * dict_rank_elec["2"]) + (
                        100 * C * dict_rank_elec["3"]) + (100 * C * dict_rank_elec["4"]) + (
                        (B - A) - 300 * C) * dict_rank_elec["5"]
            case _:
                result =  (50 * C * dict_rank_elec["1"]) + (50 * C * dict_rank_elec["2"]) + (100 * C * dict_rank_elec["3"]) + (100 * C * dict_rank_elec["4"]) + 100 * C * dict_rank_elec["5"] + ((B - A) - 400 * C) * dict_rank_elec["6"]
        str_result = f"Tiền SHBT = {result} (VNĐ)"
        self.labelDisplayMoney.setText(str_result)
        self.lineEditKWh.setText(str(B-A))
    def processContinue(self):
        self.lineEditSHBT.setText("")
        self.lineEditKWh.setText("")
        self.lineEditNewNumber.setText("")
        self.lineEditOldNumber.setText("")
    def processGuide(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Thông báo")
        dlg.setText("Đây là phần mềm tính tiền điện. Kỹ sư thiết kế: Nguyễn Bảo Huy")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Information)
        self.dlg = dlg
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Ok:
            self.dlg.close()
        else:
            pass
    def show(self):
        self.MainWindow.show()