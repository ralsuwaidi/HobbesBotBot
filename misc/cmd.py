from telegram import Update
from telegram.ext import CallbackContext
import requests
import json


def evil_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""

    response = requests.get(
        "https://evilinsult.com/generate_insult.php?")

    data = response.json()['insult']

    update.message.reply_text(data)
