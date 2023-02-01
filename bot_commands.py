from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import random

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! Введи /menu, чтобы увидеть меню!')

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/horoscope\n/recomendation\n')

async def horoscope_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/aries\n/taurus\n/gemini\n/cancer\n/leo\n/virgo\n/libra\n/scorpio\n/sagittarius\n/capricorn\n/aquarius\n/pisces\n')

async def recomendation_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    recomendation_dict = \
        {
            '1':'Не считай дни, извлекай из них пользу',
            '2':'Измени свои мысли и ты изменишь мир',
            '3':'Я не знаю секрета успеха, но секрет неудачи - это попытка всем угодить',
            '4':'Ваше время ограничено, не тратьте его на чужую жизнь',
            '5':'Не смотрите на часы; делайте то, что они делают. Не останавливайтесь',
            '6':'Будьте собой; все остальные роли уже заняты',
            '7':'Чтобы получить всю ценность радости, нужно, чтобы было с кем ее разделить',
            '8':'Если ветер не помогает, беритесь за весла',
            '9':'Куда бы вы ни шли, идите туда со всем сердцем',
            '10':'Чтобы быть лучшим, нужно уметь справляться с худшим',
        }
    key = str((random.randint(1, 11)))
    await update.message.reply_text(f'Ваш совет на {datetime.datetime.now().date()}:\n{recomendation_dict[key]}')
