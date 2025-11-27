from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def show_trading_menu(query, context):
    keyboard = [
        [InlineKeyboardButton("📊 Market Analysis", callback_data="market_analysis")],
        [InlineKeyboardButton("💹 Price Alert", callback_data="price_alert")],
        [InlineKeyboardButton("📈 Technical Indicator", callback_data="technical_indicator")],
        [InlineKeyboardButton("💰 Portfolio Tracker", callback_data="portfolio_tracker")],
        [InlineKeyboardButton("📰 News Update", callback_data="news_update")],
        [InlineKeyboardButton("⚡ Signal Trading", callback_data="trading_signal")],
        [InlineKeyboardButton("📉 Risk Management", callback_data="risk_management")],
        [InlineKeyboardButton("🧮 Profit Calculator", callback_data="profit_calculator")],
        [InlineKeyboardButton("🔍 Market Scanner", callback_data="market_scanner")],
        [InlineKeyboardButton("📚 Trading Education", callback_data="trading_education")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "📈 **Fitur Trading**\n\n"
        "Pilih fitur trading yang Anda butuhkan:",
        reply_markup=reply_markup
    )