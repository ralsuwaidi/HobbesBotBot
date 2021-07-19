from telegram import Update
from telegram.ext import CallbackContext
from misc import books
from misc.books import scrape


def books_command(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""

    book_list = []
    if len(context.args) > 0:
        update.message.reply_text('fetching books, this may take a while...')
        book_list = scrape(' '.join(context.args))
        update.message.reply_text(f'found {len(book_list)} books')
        counter = 0
        msg = ''

        if len(book_list) > 0:
            for book in book_list:
                msg = msg + f'{book.Title} - {book.Author}\n'
                counter += 1
                if counter == 5:
                    msg = msg + '...'
                    break
            update.message.reply_text(msg)

    else:
        update.message.reply_text(
            'please add the name of the book after /book')
