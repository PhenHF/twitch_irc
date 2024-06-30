import socket
from dataclasses import dataclass


from .utils import send_raw


@dataclass(frozen=True)
class TwitchConfigData:
    _NICK: str
    _PASS: str
    _HOST: str
    _PORT: int


class TwitchIRCConnect(TwitchConfigData):
    def __init__(self, _NICK: str, _PASS: str, _HOST: str, _PORT: int):
        super().__init__(_NICK, _PASS, _HOST, _PORT)
        self.__SOCKET = socket.socket()

    def __setup(self):
        self.__SOCKET.connect((self._HOST, self._PORT))
        send_raw(self.__SOCKET, 'CAP REQ :twitch.tv/tags')
        send_raw(self.__SOCKET, f'PASS oauth:{self._PASS}')
        send_raw(self.__SOCKET, f'NICK {self._NICK}')

    def connect(self) -> socket:
        self.__setup()
        return self.__SOCKET
