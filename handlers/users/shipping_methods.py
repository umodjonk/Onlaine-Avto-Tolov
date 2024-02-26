from aiogram import types
from loader import *
from data.products import *
from data.config import *


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(
            shipping_query_id=query.id,
            ok = False,
            error_message="Chet elga yetkazib bera olmaymiz"
        )
    elif query.shipping_address.city.lower()=="tashkent":
        await bot.answer_shipping_query(
            shipping_query_id=query.id, 
            shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
            ok=True
        )
    else:
        await bot.answer_shipping_query(
            shipping_query_id=query.id,
            shipping_options=[REGULAR_SHIPPING, PICKUP_SHIPPING],
            ok=True
        )

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






@dp.pre_checkout_query_handler()
async def process_pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id, ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id, text = "🥳 Xaridingiz uchun tashakkur. 😊")
    await bot.send_message(chat_id=ADMINS[0],
                            text=f"🎉 Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}✅\n"
                                f"🆔 ID: {pre_checkout_query.id}\n"
                                f"🙍‍♂️ Telegram user: {pre_checkout_query.from_user.first_name}\n"
                                f"📝 Username: @{pre_checkout_query.from_user.username}\n"
                                f"🛂 Xaridor: {pre_checkout_query.order_info.name}\n📱 Telefon: {pre_checkout_query.order_info.phone_number}")