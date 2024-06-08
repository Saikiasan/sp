from telegram import Update
from telegram.ext import ContextTypes
from fetch_product_data import fetch_product_data, get_product_data_for_gdp

async def gdp(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Fetch and send product data for a given GDP value."""
    gdp_value = ' '.join(context.args)
    if not gdp_value:
        await update.message.reply_text('Please provide a GDP value.')
        return
    
    product_data = fetch_product_data()
    if product_data is None:
        await update.message.reply_text('Failed to fetch product data.')
        return

    product = get_product_data_for_gdp(gdp_value, product_data)
    if product is None:
        await update.message.reply_text('No product data found for the given GDP value.')
        return

    product_message = (
        f"Product Data for GDP {gdp_value}:\n"
        f"Name: {product['name']}\n"
        f"Category: {product['category']}\n"
        f"Price: {product['price']}\n"
        f"Description: {product['description']}"
    )
    
    await update.message.reply_text(product_message)
