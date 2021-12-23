from telethon import events, Button, types
from ManagerUserbot import bot
from ManagerUserbot.status import is_admin
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
import time
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio

LOCKS_HELP = """
**✘ Do stickers annoy you? or want to avoid people sharing links? or pictures? You're in the right place!**
‣ `/lock` - To lock a module in the chat.
‣ `/unlock` - To unlock a module in the chat.
‣ `/locktypes` - To get a list of modules can be locked
"""

@bot.on(events.NewMessage(pattern="^[!?/]lock ?(.*)"))
@is_admin
async def lock(event, perm):
    if not perm.change_info:
      await event.reply("You are missing the following rights to use this command:CanChangeInfo")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("You haven't specified anything to lock.")
       return
    if "text" in input_str:
       await Stark.edit_permissions(event.chat_id, send_messages=False)
       await event.reply("Locked `text`.")
    elif "media" in input_str:
       await Stark.edit_permissions(event.chat_id, send_media=False)
       await event.reply("Locked `media`.")
    elif "sticker" in input_str:
       await Stark.edit_permissions(event.chat_id, send_stickers=False)
       await event.reply("Locked `sticker`.")
    elif "gifs" in input_str:
       await Stark.edit_permissions(event.chat_id, send_gifs=False)
       await event.reply("Locked `gifs`.")
    elif "forward" in input_str:
       await Stark.edit_permissions(event.chat_id, forwards=False)
       await event.reply("Locked `forward`.")
    elif "games" in input_str:
       await Stark.edit_permissions(event.chat_id, send_games=False)
       await event.reply("Locked `games`.")
    elif "inline" in input_str:
       await Stark.edit_permissions(event.chat_id, send_inline=False)
       await event.reply("Locked `inline`.")
    elif "polls" in input_str:
       await Stark.edit_permissions(event.chat_id, send_polls=False)
       await event.reply("Locked `polls`.")
    elif "preview" in input_str:
       await Stark.edit_permissions(event.chat_id, embed_link_previews=False)
       await event.reply("Locked `preview`.")
    elif "all" in input_str:
       await Stark.edit_permissions(event.chat_id,
          send_messages=False, 
          send_media=False,
          send_stickers=False,
          send_gifs=False,
          send_games=False,
          send_inline=False,
          send_polls=False,
          embed_link_previews=False)
       await event.reply("Locked `all`.")


@bot.on(events.NewMessage(pattern="^[!?/]unlock ?(.*)"))
@is_admin
async def unlock(event, perm):
    if not perm.change_info:
      await event.reply("You are missing the following rights to use this command:CanChangeInfo")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("You haven't specified anything to unlock.")
       return
    if "text" in input_str:
       await bot.edit_permissions(event.chat_id, send_messages=True)
       await event.reply("Unlocked `text`.")
    elif "media" in input_str:
       await bot.edit_permissions(event.chat_id, send_media=True)
       await event.reply("Unlocked `media`.")
    elif "sticker" in input_str:
       await bot.edit_permissions(event.chat_id, send_stickers=True)
       await event.reply("Unlocked `sticker`.")
    elif "gifs" in input_str:
       await bot.edit_permissions(event.chat_id, send_gifs=True)
       await event.reply("Unlocked `gifs`.")
    elif "forward" in input_str:
       await bot.edit_permissions(event.chat_id, forwards=True)
       await event.reply("Unlocked `forward`.")
    elif "games" in input_str:
       await bot.edit_permissions(event.chat_id, send_games=True)
       await event.reply("Unlocked `games`.")
    elif "inline" in input_str:
       await bot.edit_permissions(event.chat_id, send_inline=True)
       await event.reply("Unlocked `inline`.")
    elif "polls" in input_str:
       await bot.edit_permissions(event.chat_id, send_polls=True)
       await event.reply("Unlocked `polls`.")
    elif "preview" in input_str:
       await bot.edit_permissions(event.chat_id, embed_link_previews=True)
       await event.reply("Unlocked `preview`.")
    elif "all" in input_str:
       await bot.edit_permissions(event.chat_id,
          send_messages=True, 
          send_media=True,
          send_stickers=True,
          send_gifs=True,
          send_games=True,
          send_inline=True,
          send_polls=True,
          embed_link_previews=True)
       await event.reply("Unlocked `all`.")


@bot.on(events.NewMessage(pattern="^[!?/]locktypes"))
async def locktypes(event):
    TEXT = """
**Locks:**
‣ Text
‣ Media
‣ Sticker
‣ Gifs
‣ Videos
‣ Contacts
‣ Games
‣ Inline 
‣ all
"""
    await event.reply(TEXT)

@bot.on(events.callbackquery.CallbackQuery(data="locks"))
async def _(event):

    await event.edit(LOCKS_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])


@bot.on(events.callbackquery.CallbackQuery(data="lockss"))
async def _(event):

    await event.edit(LOCKS_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])




BANS_TEXT = """
**✘ Some people need to be publicly banned; spammers, annoyances, or just trolls.**

‣ `/kickme` - To self Kick you from a chat.
‣ `/kick` - To kick someone from a chat.
‣ `/unban` - To unban a member from the chat.
‣ `/ban` - To Ban Someone from a chat.
‣ `/dban` - To delete the replied msg and bans the user.
‣ `/sban` - To delete the replied msg and kicks the user.
‣ `/skick` - To Delete Your msg and kicks the user 
‣ `/dkick` - To delete your msg and and kicks the replied user.
"""

@bot.on(events.NewMessage(pattern="^[!?/]kick ?(.*)"))
@is_admin
async def kick(event, perm):

    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to kick him")
        return

    replied_user = msg.sender_id
    us = msg.sender.username
    info = await bot.get_entity(us)
    await bot.kick_participant(event.chat_id, input_str or replied_user)
    await event.reply(f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@bot.on(events.NewMessage(pattern="^[!?/]kickme"))
async def kickme(event):

    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return

    check = await bot.get_permissions(event.chat_id, event.sender_id)
    if check.is_admin:
        await event.reply("Sorry but I can't kick admins!")
        return

    await event.reply("Ok, as your wish")
    await bot.kick_participant(event.chat_id, event.sender_id)

@bot.on(events.NewMessage(pattern="^[!?/]ban ?(.*)"))
@is_admin
async def ban(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply("You are missing the following rights to use this command:CanBanUsers!")
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to ban him")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await bot.get_entity(us)
    await bot(EditBannedRequest(event.chat_id, replied_user, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply(f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) in {event.chat.title}")

@bot.on(events.NewMessage(pattern="^[!?/]unban ?(.*)"))
@is_admin
async def unban(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply("You are missing the following rights to use this command:CanBanUsers!")
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to unban him")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await bot.get_entity(us)
    await bot(EditBannedRequest(event.chat_id, replied_user, ChatBannedRights(until_date=None, view_messages=False)))
    await event.reply(f"Succesfully Unbanned [{info.first_name}](tg://user?id={replied_user}) in {event.chat.title}")

@bot.on(events.NewMessage(pattern="^[!?/]skick"))
@is_admin
async def skick(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete it and kick the user!")
        return

    us = reply_msg.sender.username
    info = await bot.get_entity(us)   
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await event.delete()
    await bot.kick_participant(event.chat_id, x)
    await event.reply(f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@bot.on(events.NewMessage(pattern="^[!?/]dkick"))
@is_admin
async def dkick(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete it and kick the user!")
        return
    us = reply_msg.sender.username
    info = await bot.get_entity(us) 
    x = await event.get_reply_message()
    await x.delete()
    await bot.kick_participant(event.chat_id, x.sender_id)
    await event.reply(f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@bot.on(events.NewMessage(pattern="^[!?/]dban"))
@is_admin
async def dban(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete the message and ban the user!")
        return
    us = reply_msg.sender.username
    info = await bot.get_entity(us) 
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await zx.delete()
    await bot(EditBannedRequest(event.chat_id, x, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply("Successfully Banned!")
    await event.reply(f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@bot.on(events.NewMessage(pattern="^[!?/]sban"))
@is_admin
async def sban(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete the message and ban the user!")
        return
    us = reply_msg.sender.username
    info = await bot.get_entity(us) 
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await event.delete()
    await bot(EditBannedRequest(event.chat_id, x, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply(f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@bot.on(events.callbackquery.CallbackQuery(data="bans"))
async def banhelp(event):
    await event.edit(BANS_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])

@bot.on(events.callbackquery.CallbackQuery(data="banss"))
async def banhelp(event):
    await event.edit(BANS_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])




PR_HELP = """
**✘ Need to delete lots of messages? That's what purges are for!**

‣ `/purge` - Reply to a msg to delete msgs from there.
‣ `/spurge` - Same as purge, but doesnt send the final confirmation message.
‣ `/del` - Deletes the replied to message.
"""

OWNER_ID = bot.uid
# Check if user has admin rights
async def is_administrator(user_id: int, message):
    admin = False
    async for user in bot.iter_participants(
        message.chat_id, filter=ChannelParticipantsAdmins
    ):
        if user_id == user.id or OWNER_ID or SUDO_USERS:
            admin = True
            break
    return admin


@bot.on(events.NewMessage(pattern="^/purge"))
async def purge(event):
    chat = event.chat_id
    msgs = []

    if not await is_administrator(user_id=event.sender_id, message=event):
        await event.reply("You're not an admin!")
        return

    msg = await event.get_reply_message()
    if not msg:
        await event.reply("Reply to a message to select where to start purging from.")
        return

    try:
        msg_id = msg.id
        count = 0
        to_delete = event.message.id - 1
        await bot.delete_messages(chat, event.message.id)
        msgs.append(event.reply_to_msg_id)
        for m_id in range(to_delete, msg_id - 1, -1):
            msgs.append(m_id)
            count += 1
            if len(msgs) == 100:
                await bot.delete_messages(chat, msgs)
                msgs = []

        await bot.delete_messages(chat, msgs)
        del_res = await bot.send_message(
            event.chat_id, f"Fast Purged {count} messages."
        )

        await asyncio.sleep(4)
        await del_res.delete()

    except MessageDeleteForbiddenError:
        text = "Failed to delete messages.\n"
        text += "Messages maybe too old or I'm not admin! or dont have delete rights!"
        del_res = await respond(text, parse_mode="md")
        await asyncio.sleep(5)
        await del_res.delete()


@bot.on(events.NewMessage(pattern="^/del$"))
async def delete_msg(event):

    if not await is_administrator(user_id=event.sender_id, message=event):
        await event.reply("You're not an admin!")
        return

    chat = event.chat_id
    msg = await event.get_reply_message()
    if not msg:
        await event.reply("Reply to some message to delete it.")
        return
    to_delete = event.message
    chat = await event.get_input_chat()
    rm = [msg, to_delete]
    await bot.delete_messages(chat, rm)

@bot.on(events.NewMessage(pattern="^[!?/]spurge"))
@is_admin
async def spurge(event, perm):
    if not perm.delete_messages:
         await event.reply("You are missing the following rights to use this command:CanDelMsgs!")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "Reply to a message to select where to start purging from.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)



@bot.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])

@bot.on(events.callbackquery.CallbackQuery(data="purgess"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="helpp")]])

