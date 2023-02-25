from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
# import FileHandler
import re
# import ui_ACTypeDialogBox
import ui_ACTypeWindow
from CustomizeACWindow import CustomizeACWindow
from ACManager import AC
# Electra AC protocol
ELECTRA = {
    'ON': '4275,4524,431,1729,434,647,432,1733,429,1733,433,648,430,651,432,1732,431,649,433,649,430,1729,433,648,433,650,433,1732,429,1731,431,648,434,1730,431,650,432,1730,432,648,434,1730,430,1732,431,1729,434,1730,432,1731,430,1730,433,650,431,1730,433,650,432,651,432,646,410,674,433,646,433,648,435,648,433,649,432,649,409,672,431,650,433,649,432,647,434,1728,433,1730,434,1728,432,1729,434,1728,435,1729,407,1754,433,1732,404,5362,4258,4548,434,1729,434,646,434,1728,433,1728,435,648,408,671,434,1728,434,647,435,649,435,1730,429,650,433,648,431,1732,432,1728,411,672,432,1732,404,673,436,1727,433,650,407,1754,434,1729,408,1757,431,1732,431,1727,411,1756,405,673,435,1728,432,648,434,646,437,645,436,648,407,673,409,675,409,672,434,648,434,647,433,648,433,622,458,649,432,650,430,1731,410,1729,457,1727,436,1727,434,1728,433,1729,433,1732,431,1730,430',
    'OFF': [1, 1, 1],
    'WARM': [5, 5, 5],
    'COLD': [3, 3, 3],
    'TEMP1': [3, 3, 3],
    'TEMP2': [4, 4, 4], }
# Samsung AC protocol
SAMSUNG = {'Samsung': {'ON': [0, 0, 0], 'OFF': [1, 1, 1], 'TEMP1': [3, 3, 3], 'TEMP2': [4, 4, 4], 'WARM': [5, 5, 5],
                       'COLD': [3, 3, 3]}}


class ChooseACTypeScreen(QtWidgets.QDialog):
    REGEX_PATTERN_LENGTH = 17

    def __init__(self, id_list, parent):
        super(ChooseACTypeScreen, self).__init__(parent=parent)
        self.setWindowModality(Qt.ApplicationModal)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.customize_ac_window = None
        self.ui = ui_ACTypeWindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.exist_id_list = id_list
        self.new_ac = AC()
        self.status = False  # is done successfully and data is valid
        self.ui.DonePushButton.clicked.connect(self.save_ac_of_type)

        self.status = self.get_inputs()
        if not self.status:
            del self.new_ac

    def get_inputs(self):
        state = self._get_name_input()
        if state:
            state = self._get_bt_id_input()

        return state

    def _get_name_input(self):
        nameIsValid = False
        while not nameIsValid:
            room_name, input_is_valid = QtWidgets.QInputDialog.getText(self, 'Step 1/2',
                                                                       'Please enter your room name:')
            if not input_is_valid:
                return nameIsValid
            try:
                self.new_ac.room_name = room_name
            except:
                nameIsValid = False
            else:
                nameIsValid = True
        return nameIsValid

    def _get_bt_id_input(self):
        IDIsValid = False
        input_valid = False
        while not IDIsValid:
            hc_sensor_id, input_valid = QtWidgets.QInputDialog.getText(self, 'Step 2/2',
                                                                       'Please enter the ID of the sensor that '
                                                                       'was given to you:')
            if input_valid:
                try:
                    self.new_ac.id = hc_sensor_id
                except:
                    self._showInvalidIDMessageBox()
                else:
                    if hc_sensor_id in self.exist_id_list:
                        self._showIDExistsMessageBox(hc_sensor_id)
                    else:
                        IDIsValid = True
            else:
                break
        return IDIsValid and input_valid

    @staticmethod
    def _showInvalidIDMessageBox():
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Invalid HC sensor id")
        msg.exec_()

    @staticmethod
    def _showIDExistsMessageBox(id_val):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(f"HC sensor with id = {id_val} exists in system.")
        msg.exec_()

    def save_ac_of_type(self, ac_type_commands_dict):
        if self.ui.AcTypesComboBox.currentText() == 'Electra':
            self.new_ac.commands = ELECTRA
        elif self.ui.AcTypesComboBox.currentText() == 'Samsung':
            self.new_ac.commands = SAMSUNG
        elif self.ui.AcTypesComboBox.currentText() == 'Customize...':
            self.new_ac.commands = self.on_customize_click()
        self.close()

    def on_customize_click(self):
        self.customize_ac_window = CustomizeACWindow(self)
        commands = None
        return commands

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.status = self.new_ac.commands is not None
        a0.accept()
