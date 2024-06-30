from twich_irc.service import create_listener
import os
from dotenv import load_dotenv


def main(streamer_name):
    listener = create_listener(
        os.getenv('TWITCH_NICK'),
        os.getenv('TWITCH_PASS')
    )
    listener.listen_chat(streamer_name, 4096)


if __name__ == '__main__':
    load_dotenv()
    streamer_name = input('Enter a streamer name: ')
    main(streamer_name)
