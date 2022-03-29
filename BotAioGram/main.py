from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import GetDataGoogleDrive as GD

bot = Bot(TOKEN)
dp = Dispatcher(bot)

lang = 'RU'


async def on_st(_):
    print('Панеслась!')


@dp.message_handler(commands=['start', 'help', 's', 'h'])
async def comm_start(message):
    global lang
    try:
        # kb=ReplyKeyboardMarkup(resize_keyboard=True)
        # bt1=types.KeyboardButton('RU')
        # bt2=types.KeyboardButton('EN')
        # kb.add(bt1,bt2)
        # await bot.send_message(message.from_user.id, 'Вас приветсвует бот компании WWTech.\nВыберите язык общение/Choose the language of communication',reply_markup=kb)

        kb1 = InlineKeyboardMarkup(row_whidth=1)  # resize_keyboard=True
        # bt1 = InlineKeyboardButton(text='youtube', url='https://youtube.com')
        # bt2 = InlineKeyboardButton(text='google', url='http://google.com')
        bt1 = InlineKeyboardButton(text='RU', callback_data='/ru')
        bt2 = InlineKeyboardButton(text='EN', callback_data='/en')

        kb1.add(bt1, bt2)

        await bot.send_message(message.from_user.id, 'Вас приветсвует бот компании WWTech.\n'
                                                     'Выберите язык общение/Choose the language of communication',
                               reply_markup=kb1)
        # await bot.send_message(message.from_user.id,reply_markup=kb)
    except:
        await message.reply('Что общатся с ботом напишите ему в ЛС\nhttps://t.me/TestZohanAio_bot')


@dp.message_handler(commands='r')
async def comm_(message):
    await message.answer('Клавиатура Реплай')
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = KeyboardButton('ok11')
    bt2 = KeyboardButton('ok23')
    bt3 = KeyboardButton('отправить контакт', request_contact=True)
    bt4 = KeyboardButton('отправить локацию', request_location=True)
    kb.add(bt1, bt2)
    kb.add(bt3, bt4)

    await message.answer('продолжить?', reply_markup=kb)


@dp.message_handler(commands='i')
async def comm_(message):
    # await message.answer('Клавиатура ИнЛайн')

    kb1 = InlineKeyboardMarkup(row_whidth=1)  # resize_keyboard=True
    # bt1 = InlineKeyboardButton(text='ok11')
    # bt2 = InlineKeyboardButton(text='ok23')
    bt33 = InlineKeyboardButton(text='youtube', url='https://youtube.com')
    bt44 = InlineKeyboardButton(text='google', url='http://google.com')
    # kb.add(bt1,bt2)
    kb1.add(bt33, bt44)

    await message.answer('продолжить?', reply_markup=kb1)


#    await message.answer('продолжить?')

@dp.message_handler()
async def echo_se(message):
    if message.text == 'ответь':
        await message.answer('А я- ' + message.text)
    elif message.text == 'Привет':
        await message.answer('Привет Сладёшка')
    elif message.text == 'ok11':
        await message.answer(GD.DAT,reply_markup=ReplyKeyboardRemove())
    elif message.text == 'ответь2':
        await message.reply('А я вот тебе - ' + message.text)
    else:
        await bot.send_message(message.from_user.id, 'А я <i>вот</i>  <b> тебе </b> - ' + message.text,
                               parse_mode='HTML')


@dp.callback_query_handler(text='/ru')
async def ru_call(callback):
    await callback.answer('Будем говорить по руссуки')  # всплывающее уведомление
    # await callback.answer('Будем говорить по руссуки',show_alert=True)# всплывающее уведомление c кнопкой вмещает 200симв
    # await callback.message.answer('Будем говорить по руссуки')# ответ в чат
    # await callback.answer()# эта строка говорит что колБэк закончен

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = KeyboardButton('Электрокары')
    bt2 = KeyboardButton('Тюнинг')
    bt3 = KeyboardButton('Авто')
    bt4 = KeyboardButton('Диски')
    bt5 = KeyboardButton('Сиденья')
    kb.add(bt1, bt2, bt3)
    kb.add(bt4, bt5)

    await callback.message.answer('Выберите категорию',reply_markup=kb)


@dp.callback_query_handler(text='/en')
async def ru_call(callback):
    await callback.answer('Lets speak English')

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = KeyboardButton('Electric cars')
    bt2 = KeyboardButton('Tuning')
    bt3 = KeyboardButton('Car')
    bt4 = KeyboardButton('Disks')
    bt5 = KeyboardButton('Seats')
    kb.add(bt1, bt2, bt3)
    kb.add(bt4, bt5)

    await callback.message.answer('Select a category',reply_markup=kb)


jh = '0'

executor.start_polling(dp, skip_updates=True, on_startup=on_st)

print(jh)
