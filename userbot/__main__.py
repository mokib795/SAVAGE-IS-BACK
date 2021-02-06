import glob
import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from userbot.plugins.thunder import bhok



from telethon import functions

from userbot import CMD_HNDLR, bot, ALIVE_NAME

from userbot.Config import Var
from userbot.thunderconfig import Config
from userbot.utils import finnalise, load_module, main_loader


BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT
logg = logging.getLogger("Black Lightning")
assistant_logg = logging.getLogger("Black Lightning")
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"


# It's the user you want to add (``user_id=user_to_add``).



async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        logg.info("Sucessfully Installed Everything")
    except BaseException:
        logg.warning("You Left The Group!\n\nSystem Failure")

async def cant(event):
    if event.query.user_id not in bot:
        logg.warning("Can't Access Me\n\nDisconnecting! ")
    return


async def yo(event):
    hmm = f"{DEFAULTUSER}"
    idd = Var.PRIVATE_GROUP_ID 
    wel = event.query.user_id
    if bot not in idd:
     logg.info("You Left The Group\n\nAdding You Back")
    await bot(
              functions.messages.AddChatUserRequest(
                              chat_id=idd, user_id=wel, fwd_limit=1000000
                        )
                     )
    return




if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None

    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)

        logg.info("Initialisation finished, no errors")
        logg.info("Starting Black Lightning")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        logg.info("Completed")
    else:
        bot.start()

path = "userbot/plugins/*.py"
files = glob.glob(path)
path = "userbot/plugins/thunder/*.py"
files = glob.glob(path)
if bot.disconnected():
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            finnalise(shortname.replace(".py", ""))
            logg.info(f"Disconnected From {DEFAULTUSER} Connecting To Assistant")
            bhok.run_until_disconnected()

elif bot.is_connected(): 
    for name in files:
        with open(name) as f:
           path1 = Path(f.name)
           shortname = path1.stem
           load_module(shortname.replace(".py", ""))
    path2 = "userbot/plugins/thunder/*.py"
    files = glob.glob(path2)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            finnalise(shortname.replace(".py", ""))
    bot.run_until_disconnected()
elif len(argv) not in (1, 3, 4):
    bot.disconnect()
    logg.info(f"Disconnected From {DEFAULTUSER}")



logg.info("Setup Sucessfull! ")
import os
logg.info("Sucessfully Connected To Telegram!")
logg.info("Black Lightning Installed\n\n.alive and @lightningsupport For Any Kind Of Help")



