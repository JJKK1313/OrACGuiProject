import copy
import pickle
import re


class TemperatureStates:
    COLD = 0
    WARM = 1


class AC:
    MIN_AC_SET_TEMP = 16
    MAX_AC_SET_TEMP = 30
    __slots__ = '_commands', '_room_name', '_id', '_currentSampledTemp', '_currentSetTemp', '_temperatureState', '_isOn'

    def __init__(self, room_name='', commands=None, ac_id=''):
        self._commands = commands       # Dictionary -> {'ON':'cmd1', 'OFF':'cmd2', 'HOT':'cmd3'...}
        self._id = ac_id
        self._room_name = room_name

        self._currentSampledTemp = 25
        self._currentSetTemp = 25
        self._temperatureState = TemperatureStates.WARM
        self._isOn = False

    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, new_room_name):
        if self.check_name(new_room_name):
            self._room_name = new_room_name
        else:
            raise ValueError(f"Room name mustn't be of length 0!")

    @property
    def CurrentSetTemperature(self):
        return self._currentSetTemp

    @property
    def commands(self) -> dict:
        return self._commands

    @commands.setter
    def commands(self, new_commands):
        self._commands = new_commands

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if AC.check_id(new_id):
            self._id = new_id
        else:
            raise ValueError(f"new ID of AC doesn't match the correct pattern: {new_id}")

    @staticmethod
    def check_id(ac_id: str):
        sensor_id_regex = "[0-9|A-Z]{2}:[0-9|A-Z]{2}:[0-9|A-Z]{2}:[0-9|A-Z]{2}:[0-9|A-Z]{2}:[0-9|A-Z]{2}"
        return re.fullmatch(sensor_id_regex, ac_id) is not None

    @staticmethod
    def check_name(new_name: str):
        return len(new_name) != 0

    @property
    def isOn(self):
        return self._isOn

    @isOn.setter
    def isOn(self, new_state: bool):
        assert isinstance(new_state, bool), 'new_state must be a boolean variable'
        self._isOn = new_state
        # raspberry pi Turn AC On Code:
        #
        #
        #

    @property
    def temperatureState(self):
        return self._temperatureState

    @temperatureState.setter
    def temperatureState(self, new_state: int):
        if new_state == 0:
            self._temperatureState = TemperatureStates.COLD
        else:
            self._temperatureState = TemperatureStates.WARM

    @property
    def setTemperature(self):
        return self._currentSetTemp

    @setTemperature.setter
    def setTemperature(self, new_set_temperature: int):
        assert isinstance(new_set_temperature, int), 'Temperature must be an integer within the range of [16, 30]'
        if AC.MIN_AC_SET_TEMP <= new_set_temperature <= AC.MAX_AC_SET_TEMP:
            self._currentSetTemp = new_set_temperature


class ACManager:
    MAX_AC_COUNT = 4

    def __init__(self):
        self._ac_list = [f"AC{i + 1}" for i in range(self.MAX_AC_COUNT)]
        self._ac_count = 0

    def __getitem__(self, ac_name) -> AC:
        assert ac_name in self._ac_list or f"AC{ac_name}" in self._ac_list, f"AC {ac_name} doesn't exist!"
        for i in range(len(self._ac_list)):
            if isinstance(self._ac_list[i], AC):
                if self._ac_list[i].room_name == ac_name:
                    return self._ac_list[i]
        return None

    def __len__(self):
        return len(self._ac_list)

    def __iter__(self):
        self._iter_idx = -1
        return self

    def __next__(self):
        self._iter_idx += 1
        if self._iter_idx >= len(self._ac_list):
            raise StopIteration
        else:
            return self._ac_list[self._iter_idx]

    def isFull(self):
        return self._ac_count >= ACManager.MAX_AC_COUNT

    def addAC(self, acObj: AC) -> bool:
        if self._ac_count < ACManager.MAX_AC_COUNT:
            free_spot_idx = self._findFreeSpot()
            if free_spot_idx != -1:
                self._ac_list.pop(free_spot_idx)
                self._ac_list.insert(free_spot_idx, acObj)
                self._ac_count += 1
                return True
        return False

    def _findFreeSpot(self) -> int:
        for idx, ac in enumerate(self._ac_list):
            if isinstance(ac, str):
                return idx
        return -1

    def removeACByID(self, ac_id: str):
        if idx := self._getACIdxByID(ac_id) is not None:
            self._removeACByIdx(idx)

    def _getACIdxByID(self, ac_id: str) -> {AC, None}:
        for idx, ac in enumerate(self._ac_list):
            if isinstance(ac, AC):
                if ac.id == ac_id:
                    return idx
        return None

    def getACByName(self, ac_name: str) -> {AC, None}:
        for idx, ac in enumerate(self._ac_list):
            if isinstance(ac, AC):
                if ac.room_name == ac_name:
                    return ac
        return None

    def _removeACByIdx(self, ac_idx: int):
        if ac_idx < 0 or ac_idx >= self.MAX_AC_COUNT:
            return
        self._ac_list.pop(ac_idx)
        self._ac_list.insert(ac_idx, f'AC{ac_idx + 1}')
        self._ac_count -= 1
        print(f"AC Count: {self._ac_count}")

    def removeACByName(self, ac_name: str):
        for idx, ac in enumerate(self._ac_list):
            if isinstance(ac, AC):
                if ac.room_name == ac_name:
                    self._removeACByIdx(idx)

    def getDict(self):
        return copy.copy(self._ac_list)

    def getACNames(self) -> list:
        return [ac.room_name for ac in self._ac_list if isinstance(ac, AC)]

    def getACIds(self) -> list:
        return [ac.id if isinstance(ac, AC) else None for ac in self._ac_list if ac is not None]

    def saveToFile(self):
        with open('AcData.pkl', 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def loadFromFile():
        with open('AcData.pkl', 'rb') as f:
            return pickle.load(f)
