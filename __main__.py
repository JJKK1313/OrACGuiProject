import os
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, pyqtSlot

import ui_gui
from ChooseACTypeScreen import ChooseACTypeScreen
from ACManager import ACManager, AC
from remoteControl import RemoteControl
from RemoveACDialog import RemoveACDialog


class MainWindow(QMainWindow):

    def __init__(self, parent=None, **kwargs):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = ui_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("AC Manager")

        self.buttons_array = [self.ui.ac1PushBtn, self.ui.ac2PushBtn, self.ui.ac3PushBtn, self.ui.ac4PushBtn]
        self.ac_manager = ACManager.loadFromFile() if os.path.exists('AcData.pkl') else ACManager()

        self.ui.addAcPushBtn.clicked.connect(self.userAddAc)
        self.refresh()

        self.buttons_array[0].clicked.connect(lambda: self.show_remote_control_to_ac(0))
        self.buttons_array[1].clicked.connect(lambda: self.show_remote_control_to_ac(1))
        self.buttons_array[2].clicked.connect(lambda: self.show_remote_control_to_ac(2))
        self.buttons_array[3].clicked.connect(lambda: self.show_remote_control_to_ac(3))

        self.ui.removeAcPushBtn.clicked.connect(self.removeAC)
        self.show()

    def userAddAc(self):
        if not self.ac_manager.isFull():
            dlg = ChooseACTypeScreen(self.ac_manager.getACIds(), parent=self)
            print(dlg.isModal())
            dlg.show()
            print("FINITO LA COMEDIA")
            if dlg.status:
                if self.ac_manager.addAC(acObj=dlg.new_ac):
                    self.ac_manager.saveToFile()
                    self.refresh()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Exceeding amount of ACs")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(f"You reached the maximum allowed air conditioners ({self.ac_manager.MAX_AC_COUNT}).\n"
                        "Before adding a new AC, remove one.")
            msg.exec_()

    def refresh(self):
        self.refresh_buttons()

    def refresh_buttons(self):
        for i, ac in enumerate(self.ac_manager):
            if isinstance(ac, AC):
                self.buttons_array[i].setText(ac.room_name)
                self.buttons_array[i].setEnabled(True)
            else:
                self.buttons_array[i].setText(ac)
                self.buttons_array[i].setEnabled(False)

    def show_remote_control_to_ac(self, button_idx: int):
        RemoteControl(self.ac_manager.getACByName(self.buttons_array[button_idx].text()), parent=self)

    def removeAC(self):
        dialogBox = RemoveACDialog(parent=self, ac_list=self.ac_manager.getACNames())
        if dialogBox.exec_():
            for ac in dialogBox.ACtoRemove:
                self.ac_manager.removeACByName(ac)
            self.ac_manager.saveToFile()
            self.refresh()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.ac_manager.saveToFile()
        a0.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = MainWindow()
    app.exec_()
