# import bluetooth
import threading
import time
import queue


class BTSocket:
    PORT = 1
    MAX_CHUNK_SIZE_ON_BT_CHANNEL = 50

    def __init__(self, bt_addr: str, passkey=1234):
        # self._sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        # self._sock.connect((bt_addr, self.PORT))
        self._sock = None
        self._is_run = True
        self._q = queue.Queue()

    def getRoomTemperatureCmdBT_HC05(self) -> str:
        self._sock.send("temp")
        # time.sleep(3)
        data = self._sock.recv(5)
        print("data is: ")
        print(str(data, 'cp1252'))
        return str(data, 'cp1252')

    def sendLoop(self):
        while self._is_run:
            try:
                cmd = self._q.get(timeout=2)
            except:
                pass
            else:
                self._sendCmd(cmd)
                self._q.task_done()

    def sendCmd(self, cmd: str):
        self._q.put(item=cmd)

    def _sendCmd(self, cmd):
        cmd_to_list = cmd.split(",")
        for idx in range(round(len(cmd_to_list) / self.MAX_CHUNK_SIZE_ON_BT_CHANNEL)):
            chunk = ','.join(
                cmd_to_list[idx * self.MAX_CHUNK_SIZE_ON_BT_CHANNEL: (idx + 1) * self.MAX_CHUNK_SIZE_ON_BT_CHANNEL])
            print(chunk[:len(chunk) - 1])
            print("------")
            self._sock.send(chunk)
            time.sleep(5)
            print("------------finish sending ir--------")
        self._sock.send("finish")
        print("finish")

    def closeConnection(self):
        self._is_run = False
        self._sock.close()


# def connectBT_HC05(addr):
#     #     bd_addr = '98:D3:C1:FD:AC:24'
#     port = 1
#     #     passkey = 1234
#     sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#     sock.connect((addr, port))
#     return sock
#
#
# def sendCmdBT_HC05(command):
#     sock = connectBT_HC05(addr)
#
#     if command == "temp":
#         sendTemperatureCmdBT_HC05(sock)
#     else:
#         CommandToArray = command.split(",")
#         print(len(CommandToArray))
#         for idx in range(round(len(CommandToArray) / 50)):
#             chunk = ','.join(CommandToArray[idx * 50:(idx + 1) * 50])
#             print(chunk[:len(chunk) - 1])
#             print("------")
#             sock.send(chunk)
#             time.sleep(5)
#     print("------------finish sending ir--------")
#     sock.send("finish")
#     time.sleep(5)
#     sock.close()
#     print("finish")
#
#
# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print(f"found {len(nearby_devices)} devices")
#
# # print(nearby_devices)
on_command = "4275,4524,431,1729,434,647,432,1733,429,1733,433,648,430,651,432,1732,431,649,433,649,430,1729,433,648," \
             "433,650,433,1732,429,1731,431,648,434,1730,431,650,432,1730,432,648,434,1730,430,1732,431,1729,434,1730," \
             "432,1731,430,1730,433,650,431,1730,433,650,432,651,432,646,410,674,433,646,433,648,435,648,433,649,432," \
             "649,409,672,431,650,433,649,432,647,434,1728,433,1730,434,1728,432,1729,434,1728,435,1729,407,1754,433," \
             "1732,404,5362,4258,4548,434,1729,434,646,434,1728,433,1728,435,648,408,671,434,1728,434,647,435,649,435," \
             "1730,429,650,433,648,431,1732,432,1728,411,672,432,1732,404,673,436,1727,433,650,407,1754,434,1729,408," \
             "1757,431,1732,431,1727,411,1756,405,673,435,1728,432,648,434,646,437,645,436,648,407,673,409,675,409,672," \
             "434,648,434,647,433,648,433,622,458,649,432,650,430,1731,410,1729,457,1727,436,1727,434,1728,433,1729," \
             "433," \
             "1732,431,1730,430 "
#
# command1 = "temp"
# for addr, name in nearby_devices:
#     if name == 'HC-05':
#         print(f"{addr} - {name}")
#         connectBT_HC05(addr, on_command)
