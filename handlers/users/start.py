from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states.user_states import UserMessages


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message, state: FSMContext):
    deeplink = message.text[7:]
    if deeplink:
        await message.answer(f"Salom! Yashirin xabaringizni jo'natishingiz mumkin.")
        await UserMessages.anonymous_message.set()
        await state.update_data(chat_id=deeplink)
    else:
        await message.answer(f"Salom. Bu sizning anonim chat linkingiz: https://t.me/raremebot?start={message.chat.id}")


@dp.message_handler(state=UserMessages.anonymous_message)
async def send_anonymous_message(message: types.Message, state: FSMContext):
    anonym_message = message.text
    data = await state.get_data()
    chat_id = data.get("chat_id")
    await bot.send_message(chat_id=int(chat_id), text=anonym_message)



