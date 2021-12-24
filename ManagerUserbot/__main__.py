#    Managers Userbot
#    Copyright (C) 2021 Managers Userbot




import glob
from pathlib import Path
from ManagerUserbot.utils import load_plugins
import logging
from ManagerUserbot import bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "ManagerUserbot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully Started Bot!")
print("Telah aktif")

if __name__ == "__main__":
    bot.run_until_disconnected()
