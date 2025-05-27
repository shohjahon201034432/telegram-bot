from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import WebAppInfo

TOKEN = "7969737793:AAHSl5hhYX55E7O4Twajv1j0dEQKcf-iGVw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    user_id = str(message.from_user.id)
    web_url = f"https://shohjahon201034432.github.io/tapgame/?user_id={user_id}"
    keyboard = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton("🎮 O'yinni boshlash", web_app=WebAppInfo(url=web_url))
    )
    await message.answer("🎯 TapCoin o'yiniga xush kelibsiz!", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp)
