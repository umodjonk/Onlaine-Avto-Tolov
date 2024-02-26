from aiogram import types
from aiogram.types import LabeledPrice
from utils.misc.product import Product

# Al aziz
#
# Kanaliga
#
# Obuna
#
# Boling
#


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer
iwatch = Product(
    title = "iWatch qo'l soati",
    description="Mahsulotga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="iWatch",
            amount=85000000
        ),
        LabeledPrice(
            label="Chegirma",
            amount=-1000000
        )
    ],
    start_parameter="create_invoice_iwatch",
    photo_url="https://c0.klipartz.com/pngpicture/838/816/gratis-png-apple-watch-series-3-apple-watch-series-2-apple-watch-edition-apple.png",
    photo_width=1280,
    photo_height=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)
# https://i.pinimg.com/originals/d9/44/e9/d944e9f75bc70e2139b327a2f9ed2d2c.jpg
dron = Product(
    title="Dron - Kamera",
    description="Mahsulotga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Dron",
            amount=45000000
        )
    ],
    start_parameter="create_invoice_dron",
    photo_url="https://img.favpng.com/18/8/20/mavic-pro-quadcopter-unmanned-aerial-vehicle-dji-multirotor-png-favpng-biWm6vpiFjcaFBWPeUef3zNdw.jpg",
    photo_width=1200,
    photo_height=500,
    need_email=True,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
)

microphone = Product(
    title = "RGB Microphone",
    description="Mahsulotlag to'lov qilish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Microphone",
            amount=90000000
        )
    ],
    start_parameter="create_invoice_microphone",
    photo_url="https://i.pinimg.com/originals/d9/44/e9/d944e9f75bc70e2139b327a2f9ed2d2c.jpg",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

keyboard = Product(
    title="RGB Klaviatura",
    description="Mahsulotni sotib olish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Klaviatura",
            amount=120000000
        )
    ],
    start_parameter="create_invoice_keyboard",
    photo_url="https://techbroll.com/wp-content/uploads/2020/04/A6408408-scaled.jpg",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True, 
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer



# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

costum = Product(
    title="Costum for men",
    description="Mahsulotni sotib olish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Kostyum",
            amount=120000000
        )
    ],
    start_parameter="create_invoice_costum",
    photo_url="https://i.pinimg.com/originals/6e/89/40/6e8940c13de64c221b461c68eba9344a.jpg",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True, 
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

#coat https://mixinform.com/_nw/25/63930942.jpg
#bag https://obzorus.com/wp-content/uploads/brendovie-sumki-4-min.jpg
bag = Product(
    title="Ayollar uchun sumka",
    description="Mahsulotni sotib olish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Sumka",
            amount=50000000
        )
    ],
    start_parameter="create_invoice_bag",
    photo_url="https://obzorus.com/wp-content/uploads/brendovie-sumki-4-min.jpg",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True, 
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)
coat = Product(
    title="Ayollar uchun palto",
    description="Mahsulotni sotib olish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Palto",
            amount=180000000
        )
    ],
    start_parameter="create_invoice_coat",
    photo_url="https://mixinform.com/_nw/25/63930942.jpg",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True, 
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer


REGULAR_SHIPPING = types.ShippingOption(
    id="post_reg",
    title = "Fargo (3 kun)",
    prices=[
        LabeledPrice("Maxsus quti", 1000000),
        LabeledPrice("3 ish kunida yetkazish", 1000000),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id = "post_fast",
    title = "Express pochta (1 kun)",
    prices=[
        LabeledPrice("1 kunda yetkazish", 1000000)
    ]
)
PICKUP_SHIPPING = types.ShippingOption(
    id="pickup",
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice("Yetkazib berishsiz", -1000000)
    ]
)

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

# Ushbu kod @KingsOfPy telegram kanali hisoblanada uni manbasiz tarqatish mumkin emas
# Dasturchi @Firdavs_Programmer

hamburger = Product(
    title="Ma'zali Gamburger",
    description="Mahsulotni sotib olish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Gamburger",
            amount=1200000
        )
    ],
    start_parameter="create_invoice_hamburger",
    photo_url="https://e7.pngegg.com/pngimages/121/878/png-clipart-whopper-cheeseburger-veggie-burger-hamburger-mcdonald-s-big-mac-burger-beef.png",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True, 
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)
lavash = Product(
    title="Go'shtli lavash",
    description="Mahsulotni sotib olish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Lavash",
            amount=2000000
        )
    ],
    start_parameter="create_invoice_lavash",
    photo_url="https://w7.pngwing.com/pngs/16/539/png-transparent-taco-shawarma-fast-food-doner-kebab-hamburger-hot-dog-jamon-food-recipe-street-food.png",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True, 
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)


hotdog = Product(
    title="Ma'zali hot dog",
    description="Mahsulotni sotib olish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Hot Dog",
            amount=1500000
        )
    ],
    start_parameter="create_invoice_hotdog",
    photo_url="https://www.downloadclipart.net/large/hot-dog-png-transparent.png",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True, 
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)
pitsa = Product(
    title="Pitsa",
    description="Mahsulotni sotib olish uchun quyidagi tugmani bosing.",
    currency="UZS",
    prices=[
        LabeledPrice(
            label="Pitsa",
            amount=3500000
        )
    ],
    start_parameter="create_invoice_pizza",
    photo_url="https://catherineasquithgallery.com/uploads/posts/2021-03/1614548182_9-p-pitstsa-na-belom-fone-13.jpg",
    photo_width=500,
    photo_height=500,
    need_email=True,
    need_name=True, 
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
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
