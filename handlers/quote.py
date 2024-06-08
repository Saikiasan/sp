from telegram import Update
from telegram.ext import ContextTypes

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /quote is issued."""
    await update.message.reply_text('Quote!')
