from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


OnStart = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Помощь", callback_data="help")]
])

Help = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кнопка помощи')]
])