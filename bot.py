## example

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from main import main
bot = Client(...) # api id ,hash, bottoken

def trytocode():
    return bool(1==6)

@bot.on_message(filters.private)
async def maincode(c,m):
    main()
    fo = trytocode()
    await m.reply(fo)


bot.run()
