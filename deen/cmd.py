from telegram import Update
from telegram.ext import CallbackContext
from common import utils
import os
import requests
import json


def dua(args: list, update: Update) -> str:
    """Send a message when the command /help is issued."""

    if 'morning' or 'prayer' in args:
        if args[1] == 'morning':
            file = os.path.join(os.path.dirname(__file__),
                                'resources/dua_morning.txt')
            duas = utils.get_lines(file)

            for dua in duas:
                update.message.reply_text(dua)

        if args[1] == 'prayer':
            file = os.path.join(os.path.dirname(__file__),
                                'resources/dua_prayer.txt')
            duas = utils.get_lines(file)

            for dua in duas:
                update.message.reply_text(dua)

    else:
        update.message.reply_text("add `morning`, or `prayer` after \dua")


def pray(args: list, update: Update) -> None:
    """Send a message when the command /help is issued."""

    city = 'Dubai'
    if len(args) > 1:
        if args[1] == 'abudhabi':
            city = 'Abu Dhabi'

    params = {
        "city": city,
        "country": 'United Arab Emirates',
    }

    response = requests.get(
        "http://api.aladhan.com/v1/timingsByCity?", params=params)

    data = response.json()['data']['timings']

    update.message.reply_text(f'for {city} the timings are')
    update.message.reply_text(json.dumps(data, indent=2))
