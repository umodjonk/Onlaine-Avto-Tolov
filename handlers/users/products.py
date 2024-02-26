from aiogram import types
from keyboards.inline.buttons import *
from loader import dp

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer



# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


@dp.callback_query_handler(text = "iwatch")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/iwatch.jpg")
    caption = """
📄 Nomi: ⌚️ Apple Watch
💰 Narxi: 850000
📋 Mahsulot haqida ma'lumotlar:👇👇👇

🔸iWatch
🔸Ishlashlari tez
🔸Qotmaydi
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("iwatch"))
    await call.message.delete()


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "drone")
async def dron_handler(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/dron.jpg")
    caption = """
📄 Nomi: 🛩 Dron 521
💰 Narxi: 450000
📋 Mahsulot haqida ma'lumotlar:👇👇👇

🛩 Dron sotiladi
🛩 Uchish tezligi ham yaxshi
🛩 Zaryadkasi 8 soatga yetadi
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("dron"))
    await call.message.delete()

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


@dp.callback_query_handler(text = "microphone")
async def microphone_handler(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/microphone.jpg")
    caption = """
📄 Nomi: 🎙 Mikrofon
💰 Narxi: 900000
📋 Mahsulot haqida ma'lumotlar:👇👇👇

🧩 Gamerlar va blogerlar uchun yangi mikrafon
🧩 Ovozni tiniq yozadi
🧩 RGB 
🚚 O'zbekiston bo'ylab bepul yetkazib beramiz ✅
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("microphone"))
    await call.message.delete()


@dp.callback_query_handler(text = "keyboard")
async def keyboard_handler(call: types.CallbackQuery):
    rasm = "https://techbroll.com/wp-content/uploads/2020/04/A6408408-scaled.jpg"
    caption = """
📄 Nomi: ⌨️ RGB-Klaviatura
💰 Narxi: 1 200 000 so'm 
📋 Mahsulot haqida ma'lumotlar:👇👇👇

🧩 Gamerlar va blogerlar uchun yangi rgb-klaviatura
🧩 Tez ishlaydi
🧩 RGB
🧩 7 xil rangda yonadi
    """
    # photo=rasm, caption=caption, reply_markup=build_keyboard("keyboard")
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("keyboard"))
    await call.message.delete()

@dp.callback_query_handler(text = "costum")
async def keyboard_handler(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/costum.jpg")
    caption = """
📄 Nomi: Erkaklar uchun kostyum-shim
💰 Narxi: 1 200 000 so'm 
📋 Mahsulot haqida ma'lumotlar:👇👇👇

🧩 Yigitlar uchun oqshom to'y libosi
🧩 Yangi
🧩 Ko'ylagi ham bor
🧩 Qora
    """
    # photo=rasm, caption=caption, reply_markup=build_keyboard("keyboard")
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("costum"))
    await call.message.delete()

@dp.callback_query_handler(text = "coat")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/palto.jpg")
    caption = """
📄 Nomi: Ayollar uchun qishki palto
💰 Narxi: 1 800 000
📋 Mahsulot haqida ma'lumotlar:👇👇👇

🔸 Qish uchun yaxshi libos
🔸 Qizil rangda
🔸 Garantiyasi ham bor
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("coat"))
    await call.message.delete()

@dp.callback_query_handler(text = "bag")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/sumka.jpg")
    caption = """
📄 Nomi: Ayollar uchun sumka
💰 Narxi: 500 000
📋 Mahsulot haqida ma'lumotlar:👇👇👇

🔸 Yaxshi narsa
🔸 Kattagina sumka
🔸 Qora rangda
🔸 Charmdan qilingan
    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("bag"))
    await call.message.delete()
# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "hamburger")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = "https://e7.pngegg.com/pngimages/121/878/png-clipart-whopper-cheeseburger-veggie-burger-hamburger-mcdonald-s-big-mac-burger-beef.png"
    caption = """
📄 Nomi: 🍔 Gamburger
💰 Narxi: 12 0000 so'm

    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("hamburger"))
    await call.message.delete()

@dp.callback_query_handler(text = "lavash")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = "https://w7.pngwing.com/pngs/16/539/png-transparent-taco-shawarma-fast-food-doner-kebab-hamburger-hot-dog-jamon-food-recipe-street-food.png"
    caption = """
📄 Nomi: 🍔 Gamburger
💰 Narxi: 20 0000 so'm

    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("lavash"))
    await call.message.delete()


@dp.callback_query_handler(text = "hotdog")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = "https://www.downloadclipart.net/large/hot-dog-png-transparent.png"
    caption = """
📄 Nomi: 🍔 Gamburger
💰 Narxi: 15 0000 so'm

    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("hotdog"))
    await call.message.delete()

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







@dp.callback_query_handler(text = "pitsa")
async def iwatch_uchun(call: types.CallbackQuery):
    rasm = "https://catherineasquithgallery.com/uploads/posts/2021-03/1614548182_9-p-pitstsa-na-belom-fone-13.jpg"
    caption = """
📄 Nomi: 🍔 Gamburger
💰 Narxi: 35 0000 so'm

    """
    await call.message.answer_photo(photo=rasm, caption=caption, reply_markup=build_keyboard("pitsa"))
    await call.message.delete()

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer



# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

