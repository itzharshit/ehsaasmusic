from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❰🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨❱", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❰🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨❱", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❰🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨❱", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/ARMY0071"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❰🔧 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨❱", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/ARMY0071"
                ),
                InlineKeyboardButton(
                    text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "❰➕ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥❱",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "❰➕ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥❱",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="𝙂𝙧𝙤𝙪𝙥❱", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "❰➕ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥❱",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/ARMY0071"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "❰➕ 𝘼𝙙𝙙 𝙢𝙚 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥❱",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="❰𝙊𝙬𝙣𝙚𝙧❱", url=f"https://t.me/ARMY0071"
                ),
                InlineKeyboardButton(
                    text="❰𝙂𝙧𝙤𝙪𝙥❱", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Close", callback_data="close"),
            InlineKeyboardButton(text="🔙 Go Back", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Close", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Reset Audio Volume 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Low Vol", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Medium Vol", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 High Vol", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Amplified Vol", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Custom Volume 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Go back", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼Custom Volume 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Everyone", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Admins", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Authorized Users Lists", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Go back", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Go back", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons
