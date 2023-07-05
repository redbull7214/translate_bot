from aiogram import types
from commands import check_language, translate
from loader import dp
from services import create_user, get_messages, save_message, select_user


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    """При вводе команды /start проверяет авторизован ли пользователь.
    Если да - выводит имя пользователя
    Если нет - создает пользователя в бд.
    """
    user = await select_user(message.from_user.id)

    if user:
        await message.answer(f"Добрый день {user.name}! Вы уже зарегистрированы")
    else:
        new_user = await create_user(message.from_user.id, message.from_user.first_name)
        await message.answer(f"{new_user.name} Вы успешно зарегистрировались")


@dp.message_handler(commands=["history"])
async def command_start(message: types.Message):
    """При вводе команды /history отправляет 10 последних переводов пользователя.
    Если пользователь не авторизован - сообщает об этом.
    """
    user = await select_user(message.from_user.id)
    if user:
        messages = await get_messages(user_id=user.id)
        if len(messages) == 0:
            await message.answer("У вас пока нет сообщений")

        for mes in messages:
            await message.answer(
                f"Ваше сообщение: {mes.text}\nПеревод: {mes.translated_text}"
            )
    else:
        await message.answer("Сначала зарегистрируйтесь командой старт")


@dp.message_handler()
async def echo(message: types.Message):
    """Переводит сообщение пользователя."""
    ln = await check_language(message=message.text)
    if ln == "ru":
        res = await translate(message=message.text)
        user = await select_user(message.from_user.id)
        await save_message(text=message.text, translated_text=res, user_id=user.id)
        await message.answer(res)
    else:
        await message.answer("Введите сообщение для перевода на русском языке")
