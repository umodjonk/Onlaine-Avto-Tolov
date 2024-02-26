from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text = "🛍 Mahsulotlar")
        ],
        [
            KeyboardButton(text="🔵 Biz ijtimoiy tarmoqlarda"),
            KeyboardButton(text="📞 Biz bilan bog'lanish"),
        ],
        [
            KeyboardButton(text="🏢 Bizning ofisimiz")
        ]
    ]
)