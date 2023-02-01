from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def aries_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Овна на {datetime.datetime.now().date()}:\nСмотрите по сторонам, когда переходите дорогу')

async def taurus_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Тельца на {datetime.datetime.now().date()}:\nВам сегодня точно повезет, не зевайте!')

async def gemini_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Близнецов на {datetime.datetime.now().date()}:\nДенек будет нервным, но продуктивным')

async def cancer_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Раков на {datetime.datetime.now().date()}:\nВ поисках смысла жизни не потеряйте что-то важное')

async def leo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Львов на {datetime.datetime.now().date()}:\nЛицо понаглее - и все двери откроются перед вами')

async def virgo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Дев на {datetime.datetime.now().date()}:\nМузычку погромче, и настроение поднимается')

async def libra_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Весов на {datetime.datetime.now().date()}:\nРежим "злобный хомячок" активирован')

async def scorpio_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Скорпионов на {datetime.datetime.now().date()}:\nОкружающие, конечно, идиоты, но это не повод их бить')

async def sagittarius_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Стрельцов на {datetime.datetime.now().date()}:\nСамое время расслабиться и уделить время себе любимому')

async def capricorn_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Козерогов на {datetime.datetime.now().date()}:\nВсех не перебодаешь, не стоит и пытаться')

async def aquarius_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Водолеев на {datetime.datetime.now().date()}:\nМир, может, и не совершенен, зато вы - очень даже')

async def pisces_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Гороскоп для Рыб на {datetime.datetime.now().date()}:\nСегодня в любой ситуации вы будете как рыба в воде')
