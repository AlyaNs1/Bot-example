from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select


async def set_user(telegram_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == telegram_id))

        if not user:
            session.add(User(tg_id=telegram_id))
            await session.commit()