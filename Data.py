from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/SLBotOfficial/28")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("Code Owner", url="https://t.me/SL_BOTS_TM")],
    ]

    START = """
Hey {}
Welcome to {}
If you don't trust this bot, 
1) stop reading this message
2) delete this chat
Still reading?
You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !
By @SL_BOTS_TM
    """

    HELP = """
✨ **Available Commands** ✨
/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 
Telegram Bot to generate Pyrogram and Telethon string session by @SLBotOfficial
Source Code : [Click Here](https://github.com/DARKEMPIRESL/StringSessionBot)
Framework : [Pyrogram](https://docs.pyrogram.org)
Language : [Python](https://www.python.org)
Developer : [𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊](https://t.me/SL_BOTS_TM)
    """
