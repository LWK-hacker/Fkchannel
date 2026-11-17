import asyncio
from aiogram import Bot, Dispatcher, types

# Bot token set karen
API_TOKEN = '9145449547:AAEpOjxCc5E083RxZGPBqh-Trn4wocYUz4Q'

# Bot aur dispatcher initialize karen
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Function to add fake members
async def add_fake_members(group_id, member_count):
    for i in range(member_count):
        # Yeh dummy user ID hai, aap ek real user ID use kar sakte hain
        user_id = 8460033005
        await bot.add_chat_member(group_id, user_id, invite_link=None)

# Command handler to add fake members
@dp.message_handler(commands=['addfake'])
async def add_fake_members_handler(message: types.Message):
    group_id = message.chat.id
    member_count = 10  # Jitne members add karne hain unki count
    await add_fake_members(group_id, member_count)
    await message.reply('Fake members added successfully!')

# Bot start hone ke liye
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
