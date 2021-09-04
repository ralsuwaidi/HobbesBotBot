#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import config
from deen import cmd as deen_cmd
from misc import cmd as misc_cmd

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


def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def cmd_manager(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""

    msg = update.message.text.lower().split(" ")

    if msg[0] == '1rm':
        weight = float(msg[1])
        reps = float(msg[2])
        oneRepMax = weight * (1+(reps/30))
        update.message.reply_text("{:.1f}".format(oneRepMax))
    if msg[0] == 'dua':
        deen_cmd.dua(msg, update)
    if msg[0] == 'prayer' or msg[0] == 'pray':
        deen_cmd.pray(msg, update)
    if msg[0] == 'book' or msg[0] == 'books':
        misc_cmd.book(msg, update)


def main() -> None:
    """Start the bot."""

    TOKEN = config.BOT_TOKEN

    # heroku appname
    NAME = config.HEROKU_APP_NAME

    # given by heroku
    PORT = config.PORT

    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, cmd_manager))

    # error handler
    dispatcher.add_error_handler(error)

    if config.PRODUCTION == 'TRUE':
        # for production
        updater.start_webhook(listen="0.0.0.0",
                              port=int(PORT),
                              url_path=TOKEN,
                              webhook_url=f"https://{NAME}.herokuapp.com/{TOKEN}")
    else:
        # for local development
        updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
