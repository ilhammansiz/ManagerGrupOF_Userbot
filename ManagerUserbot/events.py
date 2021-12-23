from telethon import events
from telethon.events import CallbackQuery

from ManagerUserbot import bot 

import sys



def mansiez(**args):
    """ Registers a new message. """
    pattern = args.get("pattern", None)

    r_pattern = r"^[/!]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        bot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator
