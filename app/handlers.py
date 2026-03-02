from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import app.keyboards as kb
import app.database.requests as rq

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Привет', parse_mode='HTML', reply_markup=kb.OnStart)




@router.callback_query(F.data == "help")
async def help(callback: CallbackQuery):
    await callback.message.answer("Помоги себе", reply_markup=kb.Help)