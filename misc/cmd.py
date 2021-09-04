from telegram import Update
from misc.books import scrape


def book(args: list, update: Update) -> None:
    """Echo the user message."""

    book_list = []
    if len(args) > 1:
        update.message.reply_text('fetching books, this may take a while...')
        book_list = scrape(' '.join(args[1:]))
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
