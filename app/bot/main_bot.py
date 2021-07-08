import logging

from app.bot.botTelegram.bot_filters import response_metas_complete, response_metas_incomplete
from telegram import ForceReply, Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
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
   
    if "/m" in mensage:
        text = response_metas_complete(mensage, username)
        update.message.reply_text(text)
    elif "/n" in mensage:
        text = response_metas_incomplete(mensage, username)
        update.message.reply_text(text)
    else:
        update.message.reply_text("""ERRO!!!\npara adcionar as metas do dia use o comando \ n\npara adicionar a metas concluidas use o comando \m """)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1852237008:AAFMzbuyROUQbWj3J3dO2GZbXfGX6lOJ28g")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, response))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



