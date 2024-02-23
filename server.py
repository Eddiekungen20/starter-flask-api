import sys
from gunicorn.app.wsgiapp import run
import socket
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


def send_data_to_mod(data):
    print("Sieg Heil")


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message forgor to exist")
        return
    await message.channel.send(user_message)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


def main() -> None:
    client.run(TOKEN)









if __name__ == '__main__':
    sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
    sys.exit(run())
