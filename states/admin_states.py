from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminStates(StatesGroup):
    get_url = State()
