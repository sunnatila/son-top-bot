from random import randint
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from sonFunc import sonTopUser, generateNumber, updateResult, compNumber, new_comp_number, newCompRandomNumber

TOKEN = "6119910825:AAHLqH1-HZ4LcUO0w5AHd5Dvr_zNvNp13fA"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
result = {
    'urinish': 0,
    'ok': False,
    'kattami': None,
    'number': randint(1, 10)
}

result_bot = {
    'urinish': 0,
    'ok': False,
    'halol': True,
    'a': 1,
    'b': 10,
    'number': randint(1, 10)
}


startGameButton = KeyboardButton("O'yinni boshlash")
startUserButton = KeyboardButton("Kettik")
bigButton = KeyboardButton("Katta")
smallButton = KeyboardButton("Kichik")
rightButton = KeyboardButton("To'g'ri")

gameUserMarkup = ReplyKeyboardMarkup(resize_keyboard=True).add(startUserButton)
gameReplyMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
gameReplyMarkup.add(startGameButton)
selectionReplyMarkup = ReplyKeyboardMarkup(resize_keyboard=True).row(bigButton, smallButton, rightButton)


@dp.message_handler(commands=['start'])
async def startMessage(msg: types.Message):
    await msg.reply("O'yin botiga xush kelibsiz!", reply_markup=gameReplyMarkup)


@dp.message_handler(text_contains='O\'yinni boshlash')
async def startGame(msg: types.Message):
    updateResult(result)
    await msg.answer("Men 1dan 10gacha bo'lgan sonni o'yladim uni topingchi!", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text_contains='Kettik')
async def start_user_game(msg: types.Message):
    comp_son = result_bot['number']
    await msg.answer(f"Siz {comp_son} sonini oyladingiz.", reply_markup=selectionReplyMarkup)


@dp.message_handler(text_contains='Katta')
async def bigNum(msg: types.Message):
    res = compNumber('+', result_bot)
    if res['halol']:
        son = res['number']
        await msg.answer(f"Siz {son} soninni oyladingiz.", reply_markup=selectionReplyMarkup)
    else:
        await msg.answer("Siz halol oynamadingiz ushanchun men yutim.\n Boshidan boshlang.",
                         reply_markup=gameReplyMarkup)
        new_comp_number(result_bot)


@dp.message_handler(text_contains='Kichik')
async def smallNum(msg: types.Message):
    res = compNumber('-', result_bot)
    if res['halol']:
        son = res['number']
        await msg.answer(f"Siz {son} soninni oyladingiz.", reply_markup=selectionReplyMarkup)
    else:
        await msg.answer("Siz halol oynamadingiz ushanchun men yutim.\n Boshidan boshlang.",
                         reply_markup=gameReplyMarkup)
        new_comp_number(result_bot)


@dp.message_handler(text_contains='To\'g\'ri')
async def to_griNum(msg: types.Message):
    res = compNumber('t', result_bot)
    await msg.answer(f"Men siz oylagan sonni {res['urinish']} ta urinishda topdim", reply_markup=gameReplyMarkup)
    if result['urinish'] > result_bot['urinish']:
        await msg.answer(f"Bu oyinda men yutim men {result_bot['urinish']} ta urinishda topdim")
    elif result_bot['urinish'] > result['urinish']:
        await msg.answer(f"Bu oyinda siz yutdingiz siz {result['urinish']} ta urunishda topdiz")
    else:
        await msg.answer("Durrang!!")
    new_comp_number(result_bot)


@dp.message_handler()
async def numberResult(msg: types.Message):
    son = msg.text
    if result['ok']:
        await msg.reply("O'yinni qayta boshlang")
    else:
        if len(son.split()) > 1:
            await msg.answer("Siz xato yubordingiz! Qayta jo'nating")
        else:
            if son.isdigit():
                son = int(son)
                res = sonTopUser(son, result)
                if res['ok']:
                    await msg.answer(f"Qoyil siz topdingiz va {res['urinish']} ta urinish amalgan oshirdingiz! "
                                     f"Endi siz son oylen man topaman.", reply_markup=gameUserMarkup)
                else:
                    await msg.answer(f"Men o'ylagan son bundan {'katta' if res['kattami'] else 'kichik'}.")
            else:
                await msg.reply("Siz son yubormadingiz!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
