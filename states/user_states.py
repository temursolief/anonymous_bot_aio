from aiogram.dispatcher.filters.state import State, StatesGroup


class UserMessages(StatesGroup):
	anonymous_message = State()
