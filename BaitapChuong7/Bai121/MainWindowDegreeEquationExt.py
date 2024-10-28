from LearnQHBoxLayoutWindow import Ui_MainWindow
class MainWindowFirstDegreeEquation(Ui_MainWindow):
    def __init(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.setWindowTitle("Nguyen Bao Huy Demo Layout Management")
        self.pushButtonExit.clicked.connect(self.process_exit)
        self.pushButtonClear.clicked.connect(self.process_clear)
        self.pushButtonSolution.clicked.connect(self.process_solution)
    def process_solution(self):
        a = float(self.lineEditCoefficientA.text())
        b = float(self.lineEditCoefficientB.text())
        if a == 0 and b == 0:
            self.lineEditSolution.setText("Infinities solutions")
        elif a == 0 and b!=0:
            self.lineEditSolution.setText("No solution")
        else:
            self.lineEditSolution.setText("X="+str(-b/a))

    def process_clear(self):
        self.lineEditCoefficientA.setText("")
        self.lineEditCoefficientB.setText("")
        self.lineEditSolution.setText("")
    def process_exit(self):
        self.MainWindow.close()
    def show(self):
        self.MainWindow.show()

