"""
    Telegram event handlers
"""
from telegram.ext import Dispatcher, Filters, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler

from dtb.settings import DEBUG

from tgbot.handlers.utils import files, error
from tgbot.handlers.admin import handlers as admin_handlers
from tgbot.handlers.location import handlers as location_handlers
from tgbot.handlers.onboarding import handlers
from tgbot.main import bot
from utils.states import URL_STATES


def setup_dispatcher(dp):
    conversation_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", handlers.command_start),
            CommandHandler("admin", admin_handlers.admin),
            CommandHandler("stats", admin_handlers.stats),
            CommandHandler('export_users', admin_handlers.export_users),
            CommandHandler("ask_location", location_handlers.ask_for_location),
            MessageHandler(Filters.location, location_handlers.location_handler),
        ],
        states={
            URL_STATES: [
                MessageHandler(Filters.regex(r'https://'), handlers.url_send_handler),
                MessageHandler(Filters.all, handlers.url_error_handler),
            ]
        },
        fallbacks=[
            MessageHandler(Filters.all, handlers.command_start),
        ]
    )
    dp.add_handler(conversation_handler)
    dp.add_error_handler(error.send_stacktrace_to_tg_chat)

    return dp


n_workers = 0 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=n_workers, use_context=True))
