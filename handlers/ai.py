from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def show_ai_menu(query, context):
    keyboard = [
        [InlineKeyboardButton("🤖 AI Chat", callback_data="ai_chat")],
        [InlineKeyboardButton("🖼️ AI Image Generator", callback_data="ai_image")],
        [InlineKeyboardButton("📝 AI Content Writer", callback_data="ai_writer")],
        [InlineKeyboardButton("🔍 AI Research", callback_data="ai_research")],
        [InlineKeyboardButton("🎯 AI Personal Assistant", callback_data="ai_assistant")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "🤖 **AI Tools**\n\n"
        "Pilih fitur AI yang ingin digunakan:",
        reply_markup=reply_markup
    )