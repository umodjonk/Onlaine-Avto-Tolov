from aiogram import types
from loader import db, dp, bot
from keyboards.inline.buttons import *
from data.config import *
from asyncio import sleep
from aiogram.dispatcher import FSMContext
from states.send_post import *
import os

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






@dp.message_handler(commands=['admin'], chat_id = ADMINS[0])
async def panel_handler(message: types.Message):
    photo = types.InputFile(path_or_bytesio="photos/admin2.jpg")
    await message.answer_photo(photo=photo, caption="Admin panelga xush kelibsiz!", reply_markup=admin)

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "send_post")
async def send_post(call: types.CallbackQuery):
    await call.message.edit_caption(caption="Qaysi biridan foydalanasiz?")
    await call.message.edit_reply_markup(reply_markup=forward_copy)


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "back")
async def back_to_main(call: types.CallbackQuery):
    await call.message.edit_caption(caption="Siz admin panelidasiz!")
    await call.message.edit_reply_markup(reply_markup=admin)
    

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


@dp.callback_query_handler(text = "close_panel")
async def close_panel(call: types.CallbackQuery):
    await call.answer("Admin panel yopildi!")
    await call.message.delete()

@dp.callback_query_handler(text = "statistics")
async def bot_statistics(call: types.CallbackQuery):
    rasm = types.InputFile(path_or_bytesio="photos/statistics.jpg")
    user = await bot.get_me()
    await call.answer(cache_time=1)
    niamdie = await call.message.answer_photo(photo=rasm, caption = f"Botdagi foydalanuvchilar soni: {db.count_users()[0]} ta!\n\n@{user.username}")
    await sleep(6)
    await bot.delete_message(chat_id=call.from_user.id, message_id=niamdie.message_id)
# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

# Foydalanuvchilarga post yuborish uchun handler
@dp.callback_query_handler(text = "copy_post")
async def send_post_all(call: types.CallbackQuery):
    await call.message.answer("📝 Yubormoqchi bo'lgan postingizni menga post yuboring.", reply_markup=cancel)
    await call.message.delete()
    await SendPostState.post.set()


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

@dp.callback_query_handler(text = "forward_post")
async def send_post_all(call: types.CallbackQuery):
    await call.message.answer("📝 Yubormoqchi bo'lgan postingizni menga post yuboring.", reply_markup=cancel)
    await call.message.delete()
    await ForwardPostState.post.set()


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

# Post yuborishni bekor qilish
@dp.callback_query_handler(text = "bekorqilishpost", state=SendPostState.post)
async def dfgddfgf(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Foydalanuvchilarga post yuborish bekor qilindi!")
    rasm = types.InputFile(path_or_bytesio="photos/admin2.jpg")
    await call.message.answer_photo(photo=rasm, caption="Siz admin panelidasiz", reply_markup=admin)
    await call.message.delete()
    await state.finish()

# Tekstli post yuborish
@dp.message_handler(chat_id = 1849953640, state = SendPostState.post)
async def send_post_message(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    try:
        send = 0
        cross = 0
        text = ""
        for user in users:
            try:
                await bot.copy_message(chat_id=user[1],
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
                text += f"✅ Yuborildi!\n🆔 ID: {user[1]}\n🪪 Username: {user[3]}\n📝 FullName: {user[2]}\n\n"
                send += 1
            except Exception as err:
                cross += 1
        user = await bot.get_me()

        text += f"\n✅ {send} ta foydalanuvchiga yuborildi.\n❌ {cross} ta foydalanuvchiga yuborilmadi!\n\n@{user.username}"
        deletaion = await message.answer(text=text)
        await state.finish()
        await sleep(60)
        await bot.delete_message(chat_id=message.from_user.id, message_id=deletaion.message_id)
    except Exception as err:
        await message.answer(f"{err}")

# Rasmli post yuborish
@dp.message_handler(chat_id = 1849953640, state = SendPostState.post,content_types='photo')
async def send_post_message(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    try:
        send = 0
        cross = 0
        text = ""
        for user in users:
            try:
                await bot.copy_message(chat_id=user[1],
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
                text += f"✅ Yuborildi!\n🆔 ID: {user[1]}\n🪪 Username: {user[3]}\n📝 FullName: {user[2]}\n\n"
                send += 1
            except Exception as err:
                cross += 1
        user = await bot.get_me()

        text += f"\n✅ {send} ta foydalanuvchiga yuborildi.\n❌ {cross} ta foydalanuvchiga yuborilmadi!\n\n@{user.username}"
        deletaion = await message.answer(text=text)
        await state.finish()
        await sleep(60)
        await bot.delete_message(chat_id=message.from_user.id, message_id=deletaion.message_id)
    except Exception as err:
        await message.answer(f"{err}")



# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


#Forward qilish
@dp.callback_query_handler(text = "bekorqilishpost", state=ForwardPostState.post)
async def dfgddfgf(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Foydalanuvchilarga post yuborish bekor qilindi!")
    rasm = types.InputFile(path_or_bytesio="photos/2.jpg")
    await call.message.answer_photo(photo=rasm, caption="Siz admin panelidasiz", reply_markup=admin)
    await call.message.delete()
    await state.finish()

# Tekstli post yuborish
@dp.message_handler(chat_id = 1849953640, state = ForwardPostState.post)
async def send_post_message(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    try:
        send = 0
        cross = 0
        text = ""
        for user in users:
            try:
                await bot.forward_message(chat_id=user[1],
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
                text += f"✅ Yuborildi!\n🆔 ID: {user[1]}\n🪪 Username: {user[3]}\n📝 FullName: {user[2]}\n\n"
                send += 1
            except Exception as err:
                cross += 1
        user = await bot.get_me()

        text += f"\n✅ {send} ta foydalanuvchiga yuborildi.\n❌ {cross} ta foydalanuvchiga yuborilmadi!\n\n@{user.username}"
        deletaion = await message.answer(text=text)
        await state.finish()
        await sleep(60)
        await bot.delete_message(chat_id=message.from_user.id, message_id=deletaion.message_id)
    except Exception as err:
        await message.answer(f"{err}")

# Rasmli post yuborish
@dp.message_handler(chat_id = 1849953640, state = ForwardPostState.post, content_types='photo')
async def send_post_message(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    try:
        send = 0
        cross = 0
        text = ""
        for user in users:
            try:
                await bot.copy_message(chat_id=user[1],
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
                text += f"✅ Yuborildi!\n🆔 ID: {user[1]}\n🪪 Username: {user[3]}\n📝 FullName: {user[2]}\n\n"
                send += 1
            except Exception as err:
                cross += 1
        user = await bot.get_me()

        text += f"\n✅ {send} ta foydalanuvchiga yuborildi.\n❌ {cross} ta foydalanuvchiga yuborilmadi!\n\n@{user.username}"
        deletaion = await message.answer(text=text)
        await state.finish()
        await sleep(60)
        await bot.delete_message(chat_id=message.from_user.id, message_id=deletaion.message_id)
    except Exception as err:
        await message.answer(f"{err}")

@dp.callback_query_handler(text = "sqlite")
async def sqlite_handler(call: types.CallbackQuery):
    file = types.InputFile(path_or_bytesio="data/main.db")
    user = await bot.get_me()
    await call.message.answer_document(document=file, caption=f"Database on Sqlite form.\n\n@{user.username}")
    await call.message.delete()
    rasm = types.InputFile(path_or_bytesio="photos/admin2.jpg")
    await bot.send_photo(chat_id=call.from_user.id, photo=rasm, caption="Siz admin panelidasiz.", reply_markup=admin)

@dp.callback_query_handler(text = "excel_form")
async def save_S(call: types.CallbackQuery):
    try:
        import sqlite3
        from xlsxwriter.workbook import Workbook
        workbook = Workbook('data/Excel.xlsx')
        worksheet = workbook.add_worksheet()

        conn = sqlite3.connect('data/main.db')
        c = conn.cursor()
        c.execute(f"select * from Users")
        mysel = c.execute(f"select * from Users ")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        workbook.close()
    except Exception as err:
        await call.answer(f"Bazagani excelga yozishda xatolik: \n\n{err}")
    file = types.InputFile(path_or_bytesio="data/Excel.xlsx")
    user = await bot.get_me()
    await call.message.answer_document(document=file, caption=f"Database on Excel form.\n\n@{user.username}")
    os.remove(path="data/Excel.xlsx")


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