from .twich_irc_connect import TwitchIRCConnect
from .utils import send_raw


class TwitchChatLitener:
    def __init__(self, twitch_irc_connect: TwitchIRCConnect) -> None:
        if not isinstance(twitch_irc_connect, TwitchIRCConnect):
            raise TypeError('Connect must be a instance of TwitchIrcConnect')

        self.__CONNECTION = twitch_irc_connect.connect()

    def __recv(self, bufsize: int) -> str:
        data = b''
        while True:
            part = self.__CONNECTION.recv(bufsize)
            data += part
            if len(part) < bufsize:
                break

        return data.decode()

    def __join_chanel(self, streamer_name: str) -> None:
        streamer_name_lower = streamer_name.lower()
        send_raw(self.__CONNECTION, f'JOIN #{streamer_name_lower}')

    def listen_chat(self, streamer_name: str, bufsize: int):
        self.__join_chanel(streamer_name=streamer_name)
        buffer = ''
        while True:
            buffer += self.__recv(bufsize)
            print(buffer)
