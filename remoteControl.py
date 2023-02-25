import sys
import time

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog

from ui_remoteControl import Ui_remoteControl
from ACManager import AC, TemperatureStates
from BTSocket import BTSocket


class TimerThread(QThread):
    timeout_signal = pyqtSignal(str)

    def __init__(self, timeout_time_sec: float):
        super().__init__()
        self._start = None
        self._run_flag = True
        self._timeout_time_sec = timeout_time_sec
        self._enabled = False

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, is_enabled: bool):
        assert isinstance(is_enabled, bool), f'new Enabled state of Timer Thread must be of bool type!' \
                                             f' given {type(is_enabled)}'
        if is_enabled:
            self.resetTimer()
        self._enabled = is_enabled

    def run(self):
        self.resetTimer()
        while self._run_flag:
            while self._enabled and time.time() - self._start <= self._timeout_time_sec:
                pass
            if self._enabled:
                self.timeout_signal.emit("TIMEOUT")
                self.enabled = False

    def resetTimer(self):
        self._start = time.time()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class RemoteControl(QDialog):
    CLICK_TIMEOUT_SECS = 3

    def __init__(self, ac: AC, parent=None, **kwargs):
        assert ac is not None, 'ac must not be None!'
        super(RemoteControl, self).__init__(parent=parent)
        self.setWindowTitle(ac.room_name)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  # This removes it
        self.ui = Ui_remoteControl()
        self.ui.setupUi(self)

        self.bt_socket = BTSocket(ac.id)
        self.timer = TimerThread(self.CLICK_TIMEOUT_SECS)
        self.timer.start()

        self.ui.OnOffLabel.mousePressEvent = self.on_off_click_event
        self._ac = ac
        self.ui.roomNameLabel.setText(self._ac.room_name)

        self.updateOnOffButtonState()
        self.updateTempStateSlider()
        self.ui.wantedTempLCDDisp.display(self._ac.setTemperature)
        self.ui.decreaseTempPushBtn.clicked.connect(self.decreaseTemperature)
        self.ui.increaseTempPushBtn.clicked.connect(self.increaseTemperature)
        self.ui.tempStateSlider.valueChanged.connect(self.tempStateChanged)

        self.timer.timeout_signal.connect(self.timeout_signal_event)

        self._temp_changed = False              # temperature value changed (16-30)
        self._temp_mode_changed = False         # temperature mode changed  (HOT/COLD)

        self.exec_()

    def updateOnOffButtonState(self):
        self.ui.OnOffLabel.setPixmap(QPixmap(u":/images/{}.png".format("ON" if self._ac.isOn else "OFF")))
        self.ui.functionsFrame.setEnabled(self._ac.isOn)

    def on_off_click_event(self, e):
        self.bt_socket.sendCmd(self._ac.commands["ON" if self._ac.isOn else "OFF"])
        self._ac.isOn = not self._ac.isOn
        self.updateOnOffButtonState()

    def updateSetRoomTemperatureLCD(self, temp: int):
        self.ui.wantedTempLCDDisp.display(str(temp))

    def increaseTemperature(self):
        self.timer.enabled = True
        self._temp_changed = True
        self._ac.setTemperature += 1
        self.updateSetRoomTemperatureLCD(self._ac.setTemperature)

    def decreaseTemperature(self):
        self.timer.enabled = True
        self._temp_changed = True
        self._ac.setTemperature -= 1
        self.updateSetRoomTemperatureLCD(self._ac.setTemperature)

    def updateSampledRoomTemperatureLCD(self, temp: int):
        self.ui.roomTempLCDDisp.display(str(temp))

    def tempStateChanged(self, new_state):
        self.timer.enabled = True
        self._temp_mode_changed = True
        self._ac.temperatureState = TemperatureStates.WARM if new_state else TemperatureStates.COLD

    def updateTempStateSlider(self):
        self.ui.tempStateSlider.setValue(self._ac.temperatureState)

    def timeout_signal_event(self, e):
        self.timer.enabled = False

        if self._temp_mode_changed:
            self.bt_socket.sendCmd(self._ac.commands[f'{self._ac.temperatureState}'])
            self._temp_mode_changed = False
        if self._temp_changed:
            self.bt_socket.sendCmd(self._ac.commands[f'{self._ac.CurrentSetTemperature}'])
            self._temp_changed = False

        print("Sending Command")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        # self.bt_socket.closeConnection()
        self.timer.stop()
        a0.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = RemoteControl()
    app.exec_()
