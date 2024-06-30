DEFAULT_HOST = 'irc.chat.twitch.tv'
DEFAULT_PORT = 6667


def send_raw(socket, message):
    if not isinstance(message, str):
        raise TypeError('Message must be str')
    socket.send((message + '\r\n').encode())
