import logging
import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router
from db import create_db

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def main():
    logging.basicConfig(level=logging.INFO)
    create_db()  
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
