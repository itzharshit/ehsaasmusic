import asyncio
import importlib
import os
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from config import LOG_GROUP_ID
from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSID5, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, ASSNAME5, BOT_ID, BOT_NAME, app)
from Yukki.Core.Logger.Log import (startup_delete_last, startup_edit_last,
                                   startup_send_new)
from Yukki.Core.PyTgCalls.Yukki import (pytgcalls1, pytgcalls2, pytgcalls3,
                                        pytgcalls4, pytgcalls5)
from Yukki.Database import get_active_chats, get_sudoers, remove_active_chat
from Yukki.Inline import private_panel
from Yukki.Plugins import ALL_MODULES
from Yukki.Utilities.inline import paginate_modules

loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}


async def initiate_bot():
    with console.status(
        "[magenta] 𝘽𝙤𝙤𝙩𝙞𝙣𝙜 𝙪𝙥 𝙏𝙝𝙚 𝙔𝙪𝙠𝙠𝙞 𝙈𝙪𝙨𝙞𝙘 𝘽𝙤𝙩...",
    ) as status:
        console.print("┌ [red]Clearing MongoDB cache...")
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            console.print("[red] Error while clearing Mongo DB.")
        console.print("└ [green]MongoDB Cleared Successfully!\n\n")
        ____ = await startup_send_new("Importing All Plugins...")
        status.update(
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        await asyncio.sleep(1.7)
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        await asyncio.sleep(1.2)
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "Yukki.Plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
            await asyncio.sleep(0.2)
        console.print("")
        _____ = await startup_edit_last(____, "Finalizing...")
        status.update(
            status="[bold blue]Importation Completed!",
        )
        await asyncio.sleep(2.4)
        await startup_delete_last(_____)
    console.print(
        "[bold green]Congrats!! Yukki Music Bot has started successfully!\n"
    )
    try:
        await app.send_message(
            LOG_GROUP_ID,
            "<b>Congrats!! Music Bot has started successfully!</b>",
        )
    except Exception as e:
        print(
            "Bot has failed to access the log Channel. Make sure that you have added your bot to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    a = await app.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("Promote Bot as Admin in Logger Channel")
        console.print(f"\n[red]Stopping Bot")
        return
    try:
        await ASS_CLI_1.send_message(
            LOG_GROUP_ID,
            "<b>Congrats!! Assistant Client 1 has started successfully!</b>",
        )
    except Exception as e:
        print(
            "Assistant Account 1 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    try:
        await ASS_CLI_1.join_chat("OfficialYukki")
    except:
        pass
    try:
        await ASS_CLI_2.send_message(
            LOG_GROUP_ID,
            "<b>Congrats!! Assistant Client 2 has started successfully!</b>",
        )
    except Exception as e:
        print(
            "Assistant Account 2 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    try:
        await ASS_CLI_2.join_chat("OfficialYukki")
    except:
        pass
    try:
        await ASS_CLI_3.send_message(
            LOG_GROUP_ID,
            "<b>Congrats!! Assistant Client 3 has started successfully!</b>",
        )
    except Exception as e:
        print(
            "Assistant Account 3 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    try:
        await ASS_CLI_3.join_chat("OfficialYukki")
    except:
        pass
    try:
        await ASS_CLI_4.send_message(
            LOG_GROUP_ID,
            "<b>Congrats!! Assistant Client 4 has started successfully!</b>",
        )
    except Exception as e:
        print(
            "Assistant Account 4 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    try:
        await ASS_CLI_4.join_chat("OfficialYukki")
    except:
        pass
    try:
        await ASS_CLI_5.send_message(
            LOG_GROUP_ID,
            "<b>Congrats!! Assistant Client 5 has started successfully!</b>",
        )
    except Exception as e:
        print(
            "Assistant Account 5 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    try:
        await ASS_CLI_5.join_chat("OfficialYukki")
    except:
        pass
    console.print(f"\n┌[red] Bot Started as {BOT_NAME}!")
    console.print(f"├[green] ID :- {BOT_ID}!")
    console.print(f"├[red] Assistant 1 Started as {ASSNAME1}!")
    console.print(f"├[green] ID :- {ASSID1}!")
    console.print(f"├[red] Assistant 2 Started as {ASSNAME2}!")
    console.print(f"├[green] ID :- {ASSID2}!")
    console.print(f"├[red] Assistant 3 Started as {ASSNAME3}!")
    console.print(f"├[green] ID :- {ASSID3}!")
    console.print(f"├[red] Assistant 4 Started as {ASSNAME4}!")
    console.print(f"├[green] ID :- {ASSID4}!")
    console.print(f"├[red] Assistant 5 Started as {ASSNAME5}!")
    console.print(f"└[green] ID :- {ASSID5}!")
    await pytgcalls1.start()
    await pytgcalls2.start()
    await pytgcalls3.start()
    await pytgcalls4.start()
    await pytgcalls5.start()
    await idle()
    console.print(f"\n[red]Stopping Bot")


home_text_pm = f"""𝙃𝙚𝙡𝙡𝙤, 𝙄 𝘼𝙈 𝘼𝙉 𝘼𝘿𝙑𝘼𝙉𝘾𝙀𝘿 𝙎𝙐𝙋𝙀𝙍𝙁𝘼𝙎𝙏
𝙃𝙄𝙂𝙃 𝙌𝙐𝘼𝙇𝙄𝙏𝙔 𝙑𝘾 𝙈𝙐𝙎𝙄𝘾 𝙋𝙇𝘼𝙔𝙀𝙍.

✅ 𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 :- <a href=\"https://t.me/Army0071\">🇮🇳 ᴀʀᴍy 🇮🇳</a>"""


@app.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await app.send_message(message.chat.id, text, reply_markup=keyboard)


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name[0] == "s":
            sudoers = await get_sudoers()
            text = "**__Sudo Users List of Bot:-__**\n\n"
            j = 0
            for count, user_id in enumerate(sudoers, 1):
                try:
                    user = await app.get_users(user_id)
                    user = (
                        user.first_name if not user.mention else user.mention
                    )
                except Exception:
                    continue
                text += f"➤ {user}\n"
                j += 1
            if j == 0:
                await message.reply_text("No Sudo Users")
            else:
                await message.reply_text(text)
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            m = await message.reply_text("🔎 Fetching Info!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**𝙑𝙞𝙙𝙚𝙤 𝙏𝙧𝙖𝙘𝙠 𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣**__

❇️**Title:** {title}

⏳**Duration:** {duration} Mins
👀**Views:** `{views}`
⏰**Published Time:** {published}
🎥**Channel Name:** {channel}
📎**Channel Link:** [Visit From Here]({channellink})
🔗**Video Link:** [Link]({link})

⚡️__𝙎𝙚𝙖𝙧𝙘𝙝𝙚𝙙 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 {BOT_NAME}t__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="❰🎥 𝙒𝙖𝙩𝙘𝙝 𝙔𝙤𝙪𝙩𝙪𝙗𝙚 𝙑𝙞𝙙𝙚𝙤❱", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            return await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
    out = private_panel()
    return await message.reply_text(
        home_text_pm,
    )


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """Hello {first_name},

Click on the buttons for more information.

All commands can be used with: /
""".format(
            first_name=name
        ),
        keyboard,
    )


@app.on_callback_query(filters.regex("shikhar"))
async def shikhar(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""Hello {query.from_user.first_name},

Click on the buttons for more information.

All commands can be used with: /
 """
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "Here is the help for", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❰↪️ 𝘽𝙖𝙘𝙠❱", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="❰🔄 𝘾𝙡𝙤𝙨𝙚❱", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await app.send_message(
            query.from_user.id,
            text=home_text_pm,
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
