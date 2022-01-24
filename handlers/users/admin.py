import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    await message.answer("Reklama uchun rasm yuboring")
    await state.set_state("pic")

@dp.message_handler(state="pic", content_types=types.ContentType.PHOTO)
async def reklama(msg: types.Message, state: FSMContext):
    await msg.reply("Rasm qabul qilindi\nRasm ostiga matn yuboring")
    photo=msg.photo[-1].file_id
    await state.update_data(
        {"photo": photo}
    )
    await state.set_state("caption")

@dp.message_handler(state="caption", content_types=types.ContentType.TEXT)
async def reklama(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    photo = data.get("photo")

    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_photo(chat_id=user_id,caption=msg.text, photo=photo)
        await asyncio.sleep(0.05)
    await state.finish()


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")