from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from horo import *

app = ApplicationBuilder().token("6052507235:AAG6KqjaWh5cQcURBScVHU6MaEzFMZzzpsY").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("menu", menu_command))
app.add_handler(CommandHandler("horoscope", horoscope_command))
app.add_handler(CommandHandler("recomendation", recomendation_command))
app.add_handler(CommandHandler("aries", aries_command))
app.add_handler(CommandHandler("taurus", taurus_command))
app.add_handler(CommandHandler("gemini", gemini_command))
app.add_handler(CommandHandler("cancer", cancer_command))
app.add_handler(CommandHandler("leo", leo_command))
app.add_handler(CommandHandler("virgo", virgo_command))
app.add_handler(CommandHandler("libra", libra_command))
app.add_handler(CommandHandler("scorpio", scorpio_command))
app.add_handler(CommandHandler("sagittarius", sagittarius_command))
app.add_handler(CommandHandler("capricorn", capricorn_command))
app.add_handler(CommandHandler("aquarius", aquarius_command))
app.add_handler(CommandHandler("pisces", pisces_command))

print('start server')
app.run_polling()