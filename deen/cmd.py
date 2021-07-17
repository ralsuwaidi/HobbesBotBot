from telegram import Update
from telegram.ext import CallbackContext
from common import utils
import os
import config

def dua_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""

    if context.args[0] == 'morning':
        file = os.path.join(os.path.dirname(__file__), 'resources/dua_morning.txt')
        duas = utils.get_lines(file)

        for dua in duas:
            update.message.reply_text(dua)

    if context.args[0] == 'prayer':
        file = os.path.join(os.path.dirname(__file__), 'resources/dua_prayer.txt')
        duas = utils.get_lines(file)

        for dua in duas:
            update.message.reply_text(dua)