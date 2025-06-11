import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from model import predict_toxicity
import os

# Настройка логгирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update: Update, context):
    update.message.reply_text('Привет! Я бот для фильтрации токсичных сообщений. Добавь меня в чат и я наведу там порядок')

def handle_message(update: Update, context):
    if predict_toxicity(update.message.text):
        try:
            update.message.delete()
            logger.info(f"Удалено сообщение от {update.message.from_user.id}")
        except Exception as e:
            logger.error(f"Ошибка удаления: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()