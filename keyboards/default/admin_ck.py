from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


async def admin_get_url(url):
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    key.insert(KeyboardButton(
        text="Login", web_app=WebAppInfo(
            url=f'{url}'
        )
    )
    )
    return key
