import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled

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







class ThrottlingMiddleware(BaseMiddleware):
    """
    Simple middleware
    """

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.message_throttled(message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):
        if throttled.exceeded_count <= 2:
            await message.reply("Too many requests!")
