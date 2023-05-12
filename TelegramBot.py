from aiogram import Bot, Dispatcher, executor, types
from instaBot import motivate_me, generate_quote, generate_tip
import os
import random


try:
    bot = Bot(token=os.environ.get('TEL_TOKEN'))
    dp = Dispatcher(bot)
    #myPath = ''
    paths=["./images/_20230512_004508.jpg",
           "./images/images_20230512_004044.jpg",
           "./images/images_20230512_004411.jpg",
           "./images/Motivational_20230512_034219.jpg",
           "./images/Motivational_20230512_034819.jpg",
           "./images/Motivational_20230512_034952.jpg",
           "./images/Motivational_20230512_040501.jpg",
           "./images/Motivational_20230512_040635.jpg",
           "./images/Motivational_20230512_040751.jpg",
           "./images/Motivational_20230512_041414.jpg",
           "./images/Motivational_20230512_040751.jpg",
           "./images/motivImgText_cool.png"]

except Exception as e:
    print(f'Error!!!!!!!: {e}' )

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello mi amigo!\n"
                        "If you want a picture with a motivational quote type /motivate\n"
                        "if you want just a quote type /quote\n"
                        "if you want tips for entrepreneurs type /tip")

@dp.message_handler(commands=['motivate'])
async def motivate(message: types.Message):
    path = await motivate_me()
    await bot.send_photo(chat_id=message.chat.id, photo=open(path, 'rb'))

"""" sned url images  
@dp.message_handler(commands=['urlImage'])
async def urlImage(message: types.Message):
    await message.answer_photo('https://avatars....')
"""
   
@dp.message_handler(commands=['quote'])
async def motivate(message: types.Message):
    quote = await generate_quote()
    await message.reply(quote)

@dp.message_handler(commands=['tip'])
async def motivate(message: types.Message):
    tip = await generate_tip()
    await message.reply(tip)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp)


# /motivate_me