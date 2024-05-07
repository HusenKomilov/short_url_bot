from telegram import ParseMode, Update
from telegram.ext import CallbackContext, ConversationHandler
from users.models import User
from short_url import models, utils
from utils.states import URL_STATES

from django.shortcuts import get_object_or_404, get_list_or_404


def command_start(update: Update, context: CallbackContext) -> None:
    User.get_user_and_created(update, context)
    text = "Salom"
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id=chat_id, text=text)
    # return URL_STATES


def url_send_handler(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    url = update.message.text
    short_url = models.Link.objects.create(url=url)
    domain = "http://127.0.0.1:8000/"
    context.bot.send_message(chat_id, text=f"<code><a href='{short_url.url}'>{domain}{short_url.code}</a></code>",
                             parse_mode="html")
    return URL_STATES


def url_error_handler(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    context.bot.send_message(chat_id, text="Siz url manzil yubormadingiz")
    return ConversationHandler.END
