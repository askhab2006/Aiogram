from aiogram import Router, types
from aiogram.filters import Command
from db import add_user, get_all_users

router = Router()

@router.message(Command(commands=["adduser"]))
async def cmd_adduser(message: types.Message):
    parts = message.text.split()
    if len(parts) == 3:
        name = parts[1]
        try:
            age = int(parts[2])
        except ValueError:
            await message.answer("Возраст должен быть числом!")
            return
        add_user(name, age)
        await message.answer(f"Пользователь {name} добавлен!")
    else:
        await message.answer("Используй: /adduser имя возраст")

@router.message(Command(commands=["users"]))
async def cmd_users(message: types.Message):
    users = get_all_users()
    if not users:
        await message.answer("Пока нет пользователей.")
        return
    text = "\n".join([f"{u[0]}. {u[1]} ({u[2]} лет)" for u in users])
    await message.answer(f"Список пользователей:\n{text}")
