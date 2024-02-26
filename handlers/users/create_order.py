from aiogram import types
from data.products import *
from loader import *

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

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



@dp.callback_query_handler(text = "product:keyboard")
async def keyboard_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **keyboard.generate_invoice(),
        payload="product:keyboard"
    )
    await call.answer()
    
# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "product:iwatch")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **iwatch.generate_invoice(),
        payload="product:iwatch"
    )
    await call.answer()


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "product:dron")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **dron.generate_invoice(),
        payload="product:dron"
    )
    await call.answer()

@dp.callback_query_handler(text = "product:microphone")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **microphone.generate_invoice(),
        payload="product:microphone"
    )
    await call.answer()

@dp.callback_query_handler(text = "product:costum")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **costum.generate_invoice(),
        payload="product:costum"
    )
    await call.answer()


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



@dp.callback_query_handler(text = "product:coat")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **coat.generate_invoice(),
        payload="product:coat"
    )
    await call.answer()


@dp.callback_query_handler(text = "product:bag")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **bag.generate_invoice(),
        payload="product:bag"
    )
    await call.answer()




@dp.callback_query_handler(text = "product:hamburger")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **hamburger.generate_invoice(),
        payload="product:hamburger"
    )
    await call.answer()




@dp.callback_query_handler(text = "product:lavash")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **lavash.generate_invoice(),
        payload="product:lavash"
    )
    await call.answer()




@dp.callback_query_handler(text = "product:hotdog")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **hotdog.generate_invoice(),
        payload="product:hotdog"
    )
    await call.answer()




@dp.callback_query_handler(text = "product:pitsa")
async def iwatch_invoice(call: types.CallbackQuery):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        **pitsa.generate_invoice(),
        payload="product:pitsa"
    )
    await call.answer()



# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


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

