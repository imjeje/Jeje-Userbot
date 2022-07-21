# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time
from datetime import datetime
from secrets import choice


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd.events import register
from .ping import get_readable_time

KONTOL = [5400396253, 997461844]

absen = [
    "**ʜᴀᴅɪʀ ʙᴀɴɢ** 😁",
    "**ʜᴀᴅɪʀ ʙᴀɴɢ ᴍᴀᴀᴘ ᴛᴇʟᴀᴛ** 😄",
    "**ᴏɪ ʙᴀɴɢ ᴊɪᴋᴜ ᴀᴅᴇ ᴀᴘᴇ** 😁",
    "**ʜᴀᴅɪʀ sᴀʏᴀɴɢ** 🥵",
    "**ʙᴇɴᴛᴀʀ ʙᴀɴɢ ᴋᴇᴡᴀʀᴜɴɢ ᴅᴜʟᴜ** 😭",
    "**ᴜᴅᴀʜ ᴅᴀʀɪ ᴛᴀᴅɪ ᴅɪ ᴍᴀʀɪ** 🥺",
    "**ᴏɪᴛ ᴀʙᴀɴɢ ɢᴀɴᴛᴇɴɢ ᴅᴀʜ ʜᴀᴅɪʀ ɴɪᴄʜ** 😎",
]

ayiincakep = [
    "**𝙄𝙮𝙖 𝘼𝙮𝙞𝙞𝙣 𝙂𝙖𝙣𝙩𝙚𝙣𝙜 𝘽𝙖𝙣𝙜𝙚𝙩** 😍",
    "**𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝙂𝙖𝙠 𝘼𝙙𝙖 𝙇𝙖𝙬𝙖𝙣** 😚",
    "**𝘼𝙮𝙞𝙞𝙣 𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝘼𝙠𝙪 𝙆𝙖𝙣** 😍",
    "**𝙂𝙖𝙠 𝘼𝙙𝙖 𝙎𝙖𝙞𝙣𝙜 𝙔𝙞𝙣𝙨** 😎",
    "**𝘼𝙮𝙞𝙞𝙣 𝙅𝙖𝙢𝙚𝙩 𝙏𝙖𝙥𝙞 𝘽𝙤𝙤𝙣𝙜** 😚",
]


@register(incoming=True, from_users=KONTOL, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**★ sᴀᴊɪᴋᴜ-ᴜsᴇʀʙᴏᴛ ★**\n\n★ **ᴘɪɴɢᴇʀ :** `%sms`\n★ **ᴜᴘᴛɪᴍᴇ :** `{}`\n★ **ᴏᴡɴᴇʀ :** `{}`\n★ **ɪᴅ :** `{}`" % (
        duration)
    await ping.reply(message.format(uptime, user.first_name, user.id)
                     )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@register(incoming=True, from_users=KONTOL, pattern=r"^Absen$")
async def ayiinabsen(ganteng):
    await ganteng.reply(choice(absen))


@register(incoming=True, from_users=KONTOL, pattern=r"Senja ganteng kan$")
async def ayiin(ganteng):
    await ganteng.reply(choice(ayiincakep))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "njaping": f"**Plugin:** `jikuping`\
        \n\n  »  **Perintah : **`Perintah Ini Hanya Untuk Devs Senja-Userbot Tod.`\
        \n  »  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)
