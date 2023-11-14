from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

from config import *

def edit_channel_message(update: Update, context: CallbackContext) -> None:
    if update.channel_post.media_group_id:
        print('hello')
    elif update.channel_post.text:
        updated_text = f"{update.channel_post.text}\n\n" \
                       f"{pechat}"
        context.bot.delete_message(chat_id=CHANNEL_ID, message_id=update.channel_post.message_id)
        context.bot.send_message(chat_id=CHANNEL_ID, text=updated_text, parse_mode="HTML")

    elif update.channel_post.photo:
        if update.channel_post.caption:
            updated_text = f"{update.channel_post.caption}\n\n" \
                           f"{pechat}"
        else:
            updated_text = pechat
        context.bot.delete_message(chat_id=CHANNEL_ID, message_id=update.channel_post.message_id)
        context.bot.sendPhoto(chat_id=CHANNEL_ID, photo=update.channel_post.photo[-1].file_id, caption=updated_text, parse_mode="HTML")
    elif update.channel_post.video:
        if update.channel_post.caption:
            updated_text = f"{update.channel_post.caption}\n\n" \
                           f"{pechat}"
        else:
            updated_text = pechat
        context.bot.delete_message(chat_id=CHANNEL_ID, message_id=update.channel_post.message_id)
        context.bot.send_video(chat_id=CHANNEL_ID, video=update.channel_post.video.file_id, caption=updated_text, parse_mode="HTML")

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    edited_message_handler = MessageHandler(Filters.chat(chat_id=CHANNEL_ID), edit_channel_message)
    dispatcher.add_handler(edited_message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
