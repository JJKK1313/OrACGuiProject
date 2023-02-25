from PyQt5 import QtCore, QtGui, QtWidgets
import ui_CustomizeACWindow


# Electra AC protocol

class CustomizeACWindow(QtWidgets.QDialog):

    def __init__(self, parent):
        super(CustomizeACWindow, self).__init__(parent=parent)
        self.setWindowModality(QtCore.Qt.WindowModality.WindowModal)   # block parent until window closed.
        self._brand_ac_name = None
        self.isSaved = False
        self.ui = ui_CustomizeACWindow.Ui_Form()
        self.ui.setupUi(self)

        self.ui.DoneNameGivingPushButton.clicked.connect(self.done_name_giving)
        self.ui.SavePushButton.clicked.connect(self.save_and_exit)
        self.ui.ExitPushButton.clicked.connect(self.close)
        # self.ui.CustomizeBrandNameLineEdit.clicked.connect(self.on_customize_click)

        self.ui.nameFrame.setEnabled(True)
        self.ui.recordingFrame.setEnabled(False)
        self.ui.finishFrame.setEnabled(False)

        self.show()
    
    def done_name_giving(self):
        self._brand_ac_name = self.ui.CustomizeBrandNameLineEdit.text()
        self.ui.nameFrame.setEnabled(False)
        self.ui.recordingFrame.setEnabled(True)

    def save_and_exit(self):
        # save customize ac
        self.isSaved = True
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        a0.accept()
