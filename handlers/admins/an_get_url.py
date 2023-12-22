from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin_ck import admin_get_url
from loader import dp
from states.admin_states import AdminStates


@dp.message_handler(text="/admin", state="*")
async def a_g_u_get_url(message: types.Message, state: FSMContext):
    await message.answer(
        text="Login uchun urlni kiriting:"
    )
    await AdminStates.get_url.set()


@dp.message_handler(state=AdminStates.get_url)
async def a_g_u_save_url(message: types.Message, state: FSMContext):
    await message.answer(
        text="Login tugmasini bosing",
        reply_markup=await admin_get_url(
            url=message.text
        )
    )
    await state.finish()
    