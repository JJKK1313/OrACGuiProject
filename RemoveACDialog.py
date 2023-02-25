import sys
import copy
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog

import ui_removeACDialogBox


class RemoveACDialog(QDialog):
    def __init__(self, ac_list, parent=None):
        super(RemoveACDialog, self).__init__(parent=parent)
        self.ac_list = ac_list
        self.ui = ui_removeACDialogBox.Ui_Dialog()
        self.ui.setupUi(self)
        self.checkboxes_list = [self.ui.ac1ChkBx, self.ui.ac2ChkBx, self.ui.ac3ChkBx, self.ui.ac4ChkBx]
        self.ACtoRemove = []

        for i in range(len(ac_list)):
            self.checkboxes_list[i].setChecked(False)
            self.checkboxes_list[i].setText(self.ac_list[i])

        self.checkboxes_list[0].clicked.connect(lambda: self.updateRemoveACList(self.checkboxes_list[0]))
        self.checkboxes_list[1].clicked.connect(lambda: self.updateRemoveACList(self.checkboxes_list[1]))
        self.checkboxes_list[2].clicked.connect(lambda: self.updateRemoveACList(self.checkboxes_list[2]))
        self.checkboxes_list[3].clicked.connect(lambda: self.updateRemoveACList(self.checkboxes_list[3]))

        for i in range(len(self.checkboxes_list)):
            if i >= len(self.ac_list):
                self.checkboxes_list[i].setEnabled(False)
                self.checkboxes_list[i].setText('')

        self.ui.okPushBtn.clicked.connect(self.finish)
        self.ui.cancelPushBtn.clicked.connect(self.cancel)

    def updateRemoveACList(self, chkBox):
        if chkBox.isChecked():
            self.ACtoRemove.append(chkBox.text())
        elif chkBox.text() in self.ACtoRemove:
            self.ACtoRemove.remove(chkBox.text())

    def finish(self):
        print(f"Done: {self.ACtoRemove}")
        self.accept()

    def cancel(self):
        print("Canceled")
        self.reject()
