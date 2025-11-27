from telegram import Update
from telegram.ext import ContextTypes
from database import db
from config import ADMIN_IDS

async def show_admin_menu(query, context):
    keyboard = [
        [InlineKeyboardButton("📢 Broadcast", callback_data="admin_broadcast")],
        [InlineKeyboardButton("👥 List VIP", callback_data="list_vip")],
        [InlineKeyboardButton("📊 Stats Bot", callback_data="bot_stats")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "👑 **Admin Panel**\n\n"
        "Pilih fitur admin:",
        reply_markup=reply_markup
    )

async def add_vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Hanya admin yang bisa menggunakan perintah ini.")
        return
    
    if not context.args:
        await update.message.reply_text("❌ Format: /addvip <user_id>")
        return
    
    try:
        user_id = int(context.args[0])
        db.set_vip(user_id, True)
        await update.message.reply_text(f"✅ User {user_id} berhasil ditambahkan sebagai VIP.")
    except ValueError:
        await update.message.reply_text("❌ User ID harus berupa angka.")

async def del_vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Hanya admin yang bisa menggunakan perintah ini.")
        return
    
    if not context.args:
        await update.message.reply_text("❌ Format: /delvip <user_id>")
        return
    
    try:
        user_id = int(context.args[0])
        db.set_vip(user_id, False)
        await update.message.reply_text(f"✅ User {user_id} berhasil dihapus dari VIP.")
    except ValueError:
        await update.message.reply_text("❌ User ID harus berupa angka.")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Hanya admin yang bisa menggunakan perintah ini.")
        return
    
    message = " ".join(context.args)
    if not message:
        await update.message.reply_text("❌ Format: /broadcast <pesan>")
        return
    
    # Implement broadcast logic here
    await update.message.reply_text("✅ Broadcast sedang diproses...")