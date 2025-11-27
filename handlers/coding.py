from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from config import DEEPSEEK_API_KEY

async def show_coding_menu(query, context):
    keyboard = [
        [InlineKeyboardButton("🚀 Deploy Website", callback_data="deploy_website")],
        [InlineKeyboardButton("🐛 Fix Error", callback_data="fix_error")],
        [InlineKeyboardButton("🔧 Fix Code", callback_data="fix_code")],
        [InlineKeyboardButton("🔗 Cek URL", callback_data="check_url")],
        [InlineKeyboardButton("📊 Cek EPL", callback_data="check_epl")],
        [InlineKeyboardButton("🕷️ Crawl Website", callback_data="crawl_website")],
        [InlineKeyboardButton("🛡️ Cek Keamanan Website", callback_data="website_security")],
        [InlineKeyboardButton("📱 Cek Bug WhatsApp", callback_data="whatsapp_bug")],
        [InlineKeyboardButton("❌ Cek Error JS/HTML", callback_data="check_js_error")],
        [InlineKeyboardButton("🔌 Cek API Function", callback_data="check_api")],
        [InlineKeyboardButton("🧪 Test API", callback_data="test_api")],
        [InlineKeyboardButton("🤖 AI Fix Code", callback_data="ai_fix_code")],
        [InlineKeyboardButton("💡 AI Pembuat Ide", callback_data="ai_idea")],
        [InlineKeyboardButton("📖 AI Belajar Coding", callback_data="ai_learn_code")],
        [InlineKeyboardButton("🌐 AI Pembuat Code", callback_data="ai_make_code")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "💻 **Fitur Coding & Development**\n\n"
        "Pilih fitur coding yang Anda butuhkan:",
        reply_markup=reply_markup
    )

async def ai_fix_code(update, context):
    # Implementasi AI fix code menggunakan DeepSeek API
    await update.message.reply_text("🤖 **AI Fix Code**\n\nSilakan kirim code yang ingin diperbaiki...")
    context.user_data['waiting_for_code'] = True

async def handle_code_input(update, context):
    if context.user_data.get('waiting_for_code'):
        code = update.message.text
        # Panggil DeepSeek API
        fixed_code = await call_deepseek_api(f"Perbaiki code berikut: {code}")
        await update.message.reply_text(f"✅ **Code yang Diperbaiki:**\n\n```\n{fixed_code}\n```", parse_mode='Markdown')
        context.user_data['waiting_for_code'] = False

async def call_deepseek_api(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-coder",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except:
        return "Maaf, terjadi error saat memproses permintaan."