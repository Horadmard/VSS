from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import encrypt
import decrypt

TOKEN: Final = '7466693725:AAGgIIkrIkBwTMm5gzzOhsTkkuUGo_k0il8'
BOT_USERNAME: Final = '@ccryptocupbot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there, Welcome to Crypto Bot.\n What do you wanna do?\
    1. Encrypt Text into an Image\
    2. Decrypte an Image and reach to a Text\
    3. Do nothing, Thanks for nothing!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('There is Noting we can Do!!')


async def enc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('No! i get no command from you!')


async def dec_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('No! i get no command from you!')


def handle_response(text: str) -> str:

    # print('What do you wanna do?\
    # 1. Encrypt Text into an Image\
    # 2. Decrypte an Image and reach to a Text\
    # 3. Do nothing, Thanks for nothing!')

    # inputs: list = text.split()
    choice, plain_text, image_name = text.split()

    # choice = int(input())

    if int(choice) == 1:
        # enc_command()
        # plain_text = input('Your massage:')
        # image_name = input('Image name:')
        encrypt.text_to_image(plain_text, image_name)

    elif choice == 2:
        image_name = input('Image name:')
        decrypt.image_to_text(image_name)

    # elif choice == 3:
    #     break

    else:
        print('Invalid!')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)

        else:
            return
    else:
        response: str = handle_response(text)

    print('BOT:', 'response')
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('BOT Starts ...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('enc', enc_command))
    app.add_handler(CommandHandler('dec', dec_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('BOT Polling ...')
    app.run_polling(poll_interval=5)
