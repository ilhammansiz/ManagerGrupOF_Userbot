#    ManagerUserbot
#    Copyright (C) 2021 ManagerUserbot

from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

from telethon import TelegramClient
import logging
from .Configs import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


if Config.STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(Config.STRING_SESSION), Config.APP_ID, Config.API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("ManagerUserbot", Config.APP_ID, Config.API_HASH)
