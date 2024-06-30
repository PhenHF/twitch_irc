from twich_irc.twitch_chat_listen import TwitchChatLitener, TwitchIRCConnect
from twich_irc.utils import DEFAULT_HOST, DEFAULT_PORT


def __create_connect(NICK: str = None, PASS: str = None, HOST: str = DEFAULT_HOST, PORT: int = DEFAULT_PORT) -> TwitchIRCConnect:
    new_irc_connect = TwitchIRCConnect(
        NICK,
        PASS,
        HOST,
        PORT
    )

    return new_irc_connect


def create_listener(NICK: str = None, PASS: str = None, HOST: str = DEFAULT_HOST, PORT: int = DEFAULT_PORT) -> TwitchChatLitener:
    return TwitchChatLitener(__create_connect(NICK, PASS, HOST, PORT))
