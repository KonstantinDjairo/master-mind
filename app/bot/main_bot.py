import logging

from app.bot.bot_telegram.commands_bot import *

from telegram import ForceReply, Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def response(update: Update, context: CallbackContext) -> None:
    """resonse the user message."""
    mensage = update.message.text
    username = update.effective_user.username

    if "/c" in mensage:
        text = create(mensage, username)
        update.message.reply_text(text)
    elif "/t" in mensage:
        text = task_box(mensage, username)
        update.message.reply_text(text)
    elif "/d" in mensage:
        text = done_list(mensage, username)
        update.message.reply_text(text)
    else:
        update.message.reply_text("Comando não existe")


def main() -> None:
    """Start the bot."""
    updater = Updater("1852237008:AAFMzbuyROUQbWj3J3dO2GZbXfGX6lOJ28g")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Filtra no comandos 
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, response))

    updater.start_polling()
    updater.idle()



