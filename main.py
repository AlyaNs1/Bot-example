import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main




async def main():
    await async_main()
    bot = Bot(token="") # Добавь сюда токен свой
    dp = Dispatcher()
    dp.include_router(router)
    print("Polling started")
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Отключение...')
