from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from database import db
from config import *

async def show_payment_menu(query, context):
    user_id = query.from_user.id
    balance = db.get_balance(user_id)
    
    keyboard = [
        [InlineKeyboardButton("💳 Top Up Saldo", callback_data="topup_balance")],
        [InlineKeyboardButton("📱 Beli Pulsa", callback_data="buy_pulsa")],
        [InlineKeyboardButton("📶 Beli Kuota", callback_data="buy_kuota")],
        [InlineKeyboardButton("📞 Beli NOKOS", callback_data="buy_nokos")],
        [InlineKeyboardButton("₿ Beli Bitcoin", callback_data="buy_bitcoin")],
        [InlineKeyboardButton("📱 Buat APK", callback_data="make_apk")],
        [InlineKeyboardButton("🌐 Buat Website", callback_data="make_website")],
        [InlineKeyboardButton("📊 Status Payment", callback_data="payment_status")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"💰 **Payment & Top Up**\n\n"
        f"Saldo Anda: Rp {balance:,}\n\n"
        "Pilih layanan yang diinginkan:",
        reply_markup=reply_markup
    )

async def buy_pulsa(query, context):
    if db.is_vip(query.from_user.id) or query.from_user.id in ADMIN_IDS:
        # Gratis untuk VIP/Admin
        await query.edit_message_text("✅ **Beli Pulsa**\n\nPembelian pulsa berhasil! (Gratis untuk VIP)")
    else:
        # Berbayar untuk user biasa
        await query.edit_message_text("📱 **Beli Pulsa**\n\nFitur ini berbayar. Silakan top up saldo terlebih dahulu.")

async def buy_nokos(query, context):
    keyboard = [[InlineKeyboardButton(country, callback_data=f"nokos_{country}")] for country in COUNTRIES]
    keyboard.append([InlineKeyboardButton("🔙 Kembali", callback_data="menu_payment")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "📞 **Beli NOKOS**\n\n"
        f"Harga: Rp {NOKOS_PRICE:,}\n"
        "Pilih negara:",
        reply_markup=reply_markup
    )