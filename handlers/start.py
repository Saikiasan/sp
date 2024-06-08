from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user_name = update.effective_user.first_name
    message = f" Hello! {user_name}, please feel free to explore the bot features as you deem fit."

    githubShow = f"Here is my GitHub link https://saikiasan.github.io/"
    await update.message.reply_text(message)
    await update.message.reply_text(githubShow)
    await update.message.reply_text(f"Also, you can visit my work for C.T college at https://ctctsk.in/")
    await update.message.reply_text(f"You can also contact me at 882494773")