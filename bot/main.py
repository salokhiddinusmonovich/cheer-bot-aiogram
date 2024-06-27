import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from config import BOT_TOKEN

router = Router()


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    db = Dispatcher()

    db.include_router(router)

    await db.start_polling(bot)