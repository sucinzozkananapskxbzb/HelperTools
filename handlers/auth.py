from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import CHANNEL_USERNAME, GROUP_USERNAME
from database import db

async def check_membership(query, context: ContextTypes.DEFAULT_TYPE):
    user_id = query.from_user.id
    
    # Check channel membership (simplified - in real implementation, use getChatMember)
    # This is a simplified version - you'll need to implement proper channel check
    channel_joined = True  # Replace with actual check
    group_joined = True    # Replace with actual check
    
    db.update_channel_status(user_id, channel_joined)
    db.update_group_status(user_id, group_joined)
    
    if channel_joined and group_joined:
        keyboard = [[InlineKeyboardButton("🎯 Menu Utama", callback_data="back_to_main")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "✅ **Selamat!**\n\n"
            "Anda telah memenuhi syarat keanggotaan.\n"
            "Sekarang Anda dapat menggunakan semua fitur bot.",
            reply_markup=reply_markup
        )
    else:
        keyboard = [
            [InlineKeyboardButton("✅ Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
            [InlineKeyboardButton("✅ Join Group", url=f"https://t.me/{GROUP_USERNAME}")],
            [InlineKeyboardButton("🔄 Cek Ulang", callback_data="check_membership")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "❌ **Belum Memenuhi Syarat**\n\n"
            "Anda masih harus join:\n"
            f"- Channel: {CHANNEL_USERNAME}\n"
            f"- Group: {GROUP_USERNAME}\n\n"
            "Setelah join, klik tombol 'Cek Ulang'",
            reply_markup=reply_markup
        )