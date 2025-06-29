from telegram.ext import ApplicationBuilder, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("Привет! Я бот поддержки. Напиши, что тебя тревожит.")

app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()