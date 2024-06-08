from telegram import Update
from telegram.ext import ContextTypes

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle unknown commands."""
    await update.message.reply_text("I don't understand that command. Type /help to see available commands.")
