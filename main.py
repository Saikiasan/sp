import logging
from telegram.ext import CommandHandler, MessageHandler, filters

from bot import create_bot
from handlers.start import start
from handlers.help import help_command
from handlers.quote import quote
from handlers.unknown import unknown
from handlers.gdp import gdp
from handlers.handle_keywords import handle_keywords

def main() -> None:
    """Start the bot."""
    # Replace 'YOUR_TOKEN' with the token you got from BotFather
    token = "6954122872:AAFoQj4E_kOep-J4pJ49p2-8XY6z9AM37Z8"
    
    # Initialize the bot application
    application = create_bot(token)

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("quote", quote))
    application.add_handler(CommandHandler("gdp", gdp))

    # Handle all other messages with the unknown handler
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_keywords))
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
