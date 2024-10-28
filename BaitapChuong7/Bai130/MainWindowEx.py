from Bai130.MainWindow import Ui_MainWindow
class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def processSignalAndSlot(self):
        self.pushButtonCalculateDepreciate.clicked.connect(self.processCalculateDepreciate)
        self.pushButtonDepreciateDetail.clicked.connect(self.processDepreciateDetails)

    def processDepreciateDetails(self):
        new_cost = float(self.lineEditCost.text())
        cost_delivery = float(self.lineEditCostDelivery.text())
        cost_setup = float(self.lineEditCostSetup.text())
        number_year = int(self.lineEditNumberYear.text())
        initial_cost = new_cost + cost_setup + cost_delivery
        depreciate_year = initial_cost / number_year
        result_text = ""
        temp = 0
        temp_text = ""
        for i in range(number_year):
            temp = initial_cost - depreciate_year*(i+1)
            temp_text = f"Năm {i+1}, Sau khấu hao còn => {temp}"
            result_text += temp_text + "\n"
        self.textEditDetail.setText(result_text)


    def processCalculateDepreciate(self):
        new_cost = float(self.lineEditCost.text())
        cost_delivery = float(self.lineEditCostDelivery.text())
        cost_setup = float(self.lineEditCostSetup.text())
        number_year = int(self.lineEditNumberYear.text())
        initial_cost = new_cost + cost_setup + cost_delivery
        self.lineEditInitialCost.setText(str(initial_cost))
        depreciate_year = initial_cost/number_year
        self.lineEditDepreciateYear.setText(str((depreciate_year)))
        self.lineEditDepreciateMonth.setText(str((depreciate_year/12)))

    def show(self):
        self.MainWindow.show()
