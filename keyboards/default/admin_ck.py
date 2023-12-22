from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


async def admin_get_url(url):
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    key.row("Login", WebAppInfo(url=f'{url}'))
    return key
