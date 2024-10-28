from PyQt6.QtCore import Qt

from Bai132.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.checkBoxShowImage.setChecked(True)
        self.checkBoxShowImage.stateChanged.connect(self.processChecked)
    def show(self):
        self.MainWindow.show()
    def processChecked(self,value):
        state=Qt.CheckState(value)
        if state==Qt.CheckState.Checked:
            self.labelImage.show()
        elif state==Qt.CheckState.Unchecked:
            self.labelImage.hide()