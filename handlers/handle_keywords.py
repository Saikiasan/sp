from telegram import Update
from telegram.ext import ContextTypes


async def handle_keywords(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle messages containing specific keywords."""
    text = update.message.text.lower()
    if 'work' in text:
        await update.message.reply_text("It's important to find meaningful work that you enjoy.")
    elif 'love' in text:
        await update.message.reply_text("Love is a beautiful feeling!")
    else:
        await update.message.reply_text("I'm not sure how to respond to that.")

