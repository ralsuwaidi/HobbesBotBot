from telegram import Update
from telegram.ext import CallbackContext
from common import utils
import os
import requests

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


def timing_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""

    city = 'Dubai'
    if len(context.args) >0:
        if context.args[0]=='abudhabi':
            city = 'Abu Dhabi'


    params = {
        "city": city,
        "country": 'United Arab Emirates',
    }

    response = requests.get(
        "http://api.aladhan.com/v1/timingsByCity?", params=params)

    update.message.reply_text(response.json()['data']['timings'])