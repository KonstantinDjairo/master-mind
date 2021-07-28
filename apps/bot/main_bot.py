import logging
import os
from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)
from apps.bot.bot_telegram.commands_bot import *

load_dotenv()



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
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
    """ Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def response(update: Update, context: CallbackContext) -> None:
    """ response the user message."""
    message = update.message.text
    user_name = update.effective_user.username
    id_user = update.effective_user.id

    if "/c" in message:
        text = create(message, user_name, id_user)
        update.message.reply_text(text)
    elif "/t" in message:
        text = task_box(message, user_name, id_user)
        update.message.reply_text(text)
    elif "/d" in message:
        text = done_list(message, user_name, id_user)
        update.message.reply_text(text)
    elif "/nl" in message:
        text = level(id_user)
        update.message.reply_text(text)
    else:
        update.message.reply_text("Comando não existe")


def main() -> None:
    """Start the bot."""
    TOKEN = os.getenv("TOKEN")
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on commands
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.command,
                                          response))

    updater.start_polling()
    updater.idle()



