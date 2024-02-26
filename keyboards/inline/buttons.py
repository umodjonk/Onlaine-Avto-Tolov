from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#  _  __ _
# | |/ /(_) _ __    __ _  ___
# | ' / | || '_ \  / _` |/ __|
# | . \ | || | | || (_| |\__ \
# |_|\_\|_||_| |_| \__, ||___/
#                  |___/

#          __
#   ___   / _|
#  / _ \ | |_
# | (_) ||  _|
#  \___/ |_|


#  ____          _    _
# |  _ \  _   _ | |_ | |__    ___   _ __
# | |_) || | | || __|| '_ \  / _ \ | '_ \
# |  __/ | |_| || |_ | | | || (_) || | | |
# |_|     \__, | \__||_| |_| \___/ |_| |_|
#         |___/

#  _                          _  _
# | | __  __ _  _ __    __ _ | |(_)  __ _   __ _
# | |/ / / _` || '_ \  / _` || || | / _` | / _` |
# |   < | (_| || | | || (_| || || || (_| || (_| |
# |_|\_\ \__,_||_| |_| \__,_||_||_| \__, | \__,_|
#                                   |___/

#         _
#   ___  | |__   _   _  _ __    __ _
#  / _ \ | '_ \ | | | || '_ \  / _` |
# | (_) || |_) || |_| || | | || (_| |
#  \___/ |_.__/  \__,_||_| |_| \__,_|


#  _             _  _  _
# | |__    ___  ( )| |(_) _ __    __ _
# | '_ \  / _ \ |/ | || || '_ \  / _` |
# | |_) || (_) |   | || || | | || (_| |
# |_.__/  \___/    |_||_||_| |_| \__, |
#                                |___/



electronics = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "⌚️ iWatch",
                callback_data="iwatch"
            ),
            InlineKeyboardButton(
                text="🛩 Dron 521",
                callback_data="drone"
            )
        ],
        [
            InlineKeyboardButton(
                text = "🎙 Mikrofon",
                callback_data="microphone"
            ),
            InlineKeyboardButton(
                text = "⌨️ RGB - Klaviatura",
                callback_data="keyboard"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Orqaga",
                callback_data="back_to_main"
            )
        ]
    ]
)


clothes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "🤵 Kostyum-shim (erkaklarga)",
                callback_data="costum"
            ),
            InlineKeyboardButton(
                text = "🧥 Palto (ayollarga)",
                callback_data="coat"
            )
        ],
        [
            InlineKeyboardButton(
                text="👜 Sumka (ayollarga)",
                callback_data="bag"
            )
        ],
        [
            InlineKeyboardButton(
                text = "🔙 Orqaga",
                callback_data="back_to_main"
            )
        ]
    ]
)


foods = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "🍔 Gamburger",
                callback_data="hamburger"
            ),
            InlineKeyboardButton(
                text = "🫔 Lavash",
                callback_data="lavash"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌭Hot Dog",
                callback_data="hotdog"
            ),
            InlineKeyboardButton(
                text="🍕 Pitsa",
                callback_data="pitsa"
            )
        ],
        [
            InlineKeyboardButton(
                text = "🔙 Orqaga",
                callback_data="back_to_main"
            )
        ]
    ]
)


categories = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "👕 Kiyimlar",
                callback_data="clothes"
            ),
            InlineKeyboardButton(
                text = "🔌 Elektronika",
                callback_data="electronics"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥩 Oziq-ovqat",
                callback_data="foods"
            )
        ]
    ]
)


def build_keyboard(product):
    keys = InlineKeyboardMarkup(
        inline_keyboard=[
            [
            InlineKeyboardButton(text = "🛒 Sotib olish", callback_data=f"product:{product}")
            ],
            [
            InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")
            ]
        ]
    )
    return keys

smm_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "🔵 Telegram",
                url="https://t.me/Firdavs_Yorkulov"
            )
        ],
        [
            InlineKeyboardButton(
                text = "🔴 You Tube",
                url = "https://www.youtube.com/@firdavsyorkulov192"
            )
        ],
        [
            InlineKeyboardButton(
                text="🟣 Instagram",
                url="https://www.instagram.com/firdavs_programmer"
            )
        ],
        [
            InlineKeyboardButton(
                text = "⚫️ Github",
                url = "https://github.com/FirdavsCoder"
            )
        ]
    ]
)


admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "📝 Xabar yuborish",
                callback_data="send_post"
            ),
            InlineKeyboardButton(
                text="📊 Bot statistikasi",
                callback_data="statistics"
            )
        ],
        [
            InlineKeyboardButton(
                text="🗄 Bazani yuklab olish",
                callback_data="down_base"
            )  
        ],
        [
            InlineKeyboardButton(
                text="❌ Panelni yopish",
                callback_data="close_panel"
            )
        ]
    ]
)

base = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "📝 Excel formatda",
                callback_data="excel_form"
            ),
            InlineKeyboardButton(
                text = "📂 SqLite formatda",
                callback_data="sqlite"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Orqaga",
                callback_data="back"
            ),
            InlineKeyboardButton(
                text = "❌ Yopish",
                callback_data="close_panel"
            )
        ]
    ]
)

forward_copy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📝 Forward qilish",
                callback_data="forward_post"
            ),
            InlineKeyboardButton(
                text="📝 Copy qilish",
                callback_data="copy_post"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Orqaga",
                callback_data="back"
            ),
            InlineKeyboardButton(
                text="❌ Yopish",
                callback_data="close_panel"
            )
        ]
    ],
)

cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text = "🔙 Orqaga",
                callback_data="bekorqilishpost"
            )
        ]
    ]
)