import os.path

from PyQt5 import QtCore, QtGui, QtWidgets
import ui_CustomACDialogBox
from ACManager import AC
from BTSocket import BTSocket
import pickle


class CustomizeACWindow(QtWidgets.QDialog):
    AC_COMMANDS_FILE = 'ACCommands.pkl'

    def __init__(self, ac: AC, parent):
        super(CustomizeACWindow, self).__init__(parent=parent)
        self._brand_ac_name = None
        self.isSaved = False
        self.ui = ui_CustomACDialogBox.Ui_CustomACDialogBox()
        self.ui.setupUi(self)
        self.commands = dict()

        self.bt_socket = BTSocket(ac.id)
        self.ui.DoneNameGivingPushButton.clicked.connect(self.done_name_giving)
        self.ui.SavePushButton.clicked.connect(self.save_and_exit)
        self.ui.ExitPushButton.clicked.connect(self.close)

        self.ui.nameFrame.setEnabled(True)
        self.ui.recordingFrame.setEnabled(False)
        self.ui.finishFrame.setEnabled(False)
        self.ui.commandLabel.setText('')

        self.load_commands()

        self.show()

    def load_commands(self):
        if os.path.isfile(self.AC_COMMANDS_FILE):
            with open(self.AC_COMMANDS_FILE, 'rb') as f:
                self.commands = pickle.load(f)

    def done_name_giving(self):
        self._brand_ac_name = self.ui.CustomizeBrandNameLineEdit.text()
        self.commands[self._brand_ac_name] = dict()
        self.ui.nameFrame.setEnabled(False)
        self.ui.recordingFrame.setEnabled(True)
        self.recordProcedure()

    def recordProcedure(self):
        for cmdLbl in ['ON', 'Cold', 'Warm', *(f'{i}' for i in range(16, 31)), 'OFF']:
            self.ui.commandLabel.setText(cmdLbl)
            self.recordRemote(cmdLbl)
        self.ui.recordingFrame.setEnabled(False)
        self.ui.finishFrame.setEnabled(True)

    def recordRemote(self, cmd):
        # here make LED RED or Green
        # code...
        #
        #
        # here record the IR and save to commands
        # ...record code...
        # UNCOMMENT BELLOW LINE
        # self.commands[self._brand_ac_name][cmd] =  # add here the string of the command
        #
        pass

    def save_and_exit(self):
        with open(self.AC_COMMANDS_FILE, 'wb') as f:
            pickle.dump(self.commands, f)
        self.isSaved = True
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if not self.isSaved:
            self.commands.pop(self._brand_ac_name)
        a0.accept()
