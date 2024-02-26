from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from keyboards.default.main import * 
from loader import dp, db, bot
from keyboards.inline.buttons import *
from data.products import *


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






# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if db.check_user(user_id=message.from_user.id):
                    await message.answer(f"Salom, {message.from_user.get_mention()}!🙂\n\n🧑‍💻Dasturchi: @Firdavs_Yorkulov ✔️\n🤖 @onl1ne_shopbot ushbu botimizdan ham foydalanib ko'ring!", reply_markup=main)
    else:
        try:
            db.add_user(
                user_id=message.from_user.id,
                user_fullname=message.from_user.full_name,
                username=message.from_user.username
            )
            matn = f"🎉 Yangi foydalanuvchi\n"
            matn += f"🪪 Name: {message.from_user.full_name}\n"
            matn += f"🆔 ID: {message.from_user.id}\n"
            matn += f"📝 Username: @{message.from_user.username}\n\n"
            matn += f"📊 Bazada {db.count_users()[0]} ta foydalanuvchi mavjud."
            await bot.send_message(chat_id=ADMINS[0], text=matn)
            await message.answer(f"Salom, {message.from_user.get_mention()}!🙂\n\n🧑‍💻Dasturchi: @Firdavs_Yorkulov ✔️\n🤖 @onl1ne_shopbot ushbu botimizdan ham foydalanib ko'ring!", reply_markup=main)
        except Exception as err:
            await bot.send_message(chat_id=ADMINS[0], text = err)



# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer



# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


rasm = "https://www.phanmemninja.com/wp-content/uploads/2019/05/banhangtrenshopee.png"
@dp.message_handler(text = "🛍 Mahsulotlar")
async def products_handler(message: types.Message):
    await message.answer_photo(photo=rasm, caption="Mahsulot bo'limini tanglang", reply_markup=categories)

@dp.callback_query_handler(text = "electronics")
async def electronics_handler(call: types.CallbackQuery):
    await call.message.edit_caption(caption="Mahsulot tanglang:")
    await call.message.edit_reply_markup(reply_markup=electronics)

@dp.callback_query_handler(text = "back_to_main")
async def back_handler(call: types.CallbackQuery):
    await call.message.answer_photo(photo=rasm, caption="Kategoriyalardan birini tanlang:", reply_markup=categories)
    await call.message.delete()

@dp.callback_query_handler(text = "clothes")
async def electronics_handler(call: types.CallbackQuery):
    await call.message.edit_caption(caption="Mahsulot tanglang:")
    await call.message.edit_reply_markup(reply_markup=clothes)


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer



# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


@dp.callback_query_handler(text = "foods")
async def electronics_handler(call: types.CallbackQuery):
    await call.message.edit_caption(caption="Mahsulot tanglang:")
    await call.message.edit_reply_markup(reply_markup=foods)
# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer
@dp.message_handler(text = "🔵 Biz ijtimoiy tarmoqlarda")
async def smm_handler(message: types.Message):
    await message.answer(text="Sahifalarimiz: ", reply_markup=smm_buttons)


@dp.message_handler(text ="📞 Biz bilan bog'lanish")
async def connect_handler(message: types.Message):
    await message.answer("👩🏻‍💻Biz bilan bog'lanish:\n\n📲 Telefon raqam: +998 (93) 165 1884\n👨🏻‍💻Online admin: https://t.me/firdavs_programmer")
# 39.879866137981665, 67.49403445297493

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.message_handler(text = "🏢 Bizning ofisimiz")
async def location_handler(message: types.Message):
    await message.answer("Bizning aslida mavjud bo'lmagan ofisimiz.")
    await bot.send_location(chat_id=message.from_user.id, latitude=39.879866137981665, longitude=67.49403445297493,)


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "down_base")
async def base_handler(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=base)


