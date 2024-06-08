import logging
from telegram.ext import ApplicationBuilder

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def create_bot(token: str):
    """Create and return the bot application."""
    return ApplicationBuilder().token(token).build()
