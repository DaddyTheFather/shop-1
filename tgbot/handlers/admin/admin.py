from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode

from tgbot.filters.admin import AdminFilter
from tgbot.misc.messages import AdminMessages
from tgbot.keyboards.user_inline import UserKeyboards

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(
        text="Welcome to our Shop!", reply_markup=UserKeyboards.menu_keyboard()
    )