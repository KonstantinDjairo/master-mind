import logging

from app.bot.botTelegram.bot_filters import (chek_profile, create_profile,
                                             response_metas_complete,
                                             response_metas_incomplete)
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
    
    profile = chek_profile(username)
    if "/c" in mensage:
        text = create_profile(username)
        update.message.reply_text(text)
    elif "/t" in mensage:
        if profile:
            text = response_metas_complete(mensage, username)
            update.message.reply_text(text)
        else:
            update.message.reply_text("Faça um perfil com /c")
    elif "/d" in mensage:
        if profile:
            text = response_metas_incomplete(mensage, username)
            update.message.reply_text(text)
        else:
            update.message.reply_text("Faça um perfil com /c")
    else:
        update.message.reply_text("ERRO!!!\nPara adicionar as metas do dia use o comando \d\npara adicionar a metas concluidas use o comando \t ")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1852237008:AAFMzbuyROUQbWj3J3dO2GZbXfGX6lOJ28g")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Filtra no comandos 
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.command, response))

    # Start the Bot
    updater.start_polling()
    updater.idle()



