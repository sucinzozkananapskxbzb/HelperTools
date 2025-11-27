from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random

async def show_fun_menu(query, context):
    keyboard = [
        [InlineKeyboardButton("😂 Random Joke", callback_data="random_joke")],
        [InlineKeyboardButton("🎮 Mini Games", callback_data="mini_games")],
        [InlineKeyboardButton("🔮 Fortune Teller", callback_data="fortune_teller")],
        [InlineKeyboardButton("🎵 Music Player", callback_data="music_player")],
        [InlineKeyboardButton("📸 Photo Editor", callback_data="photo_editor")],
        [InlineKeyboardButton("🎭 Quotes Harian", callback_data="daily_quotes")],
        [InlineKeyboardButton("📚 Cerita Pendek", callback_data="short_stories")],
        [InlineKeyboardButton("🎯 Tebak Gambar", callback_data="guess_image")],
        [InlineKeyboardButton("🧩 Puzzle", callback_data="puzzle_game")],
        [InlineKeyboardButton("🎲 Dadu & Koin", callback_data="dice_coin")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "😊 **Fun Menu**\n\n"
        "Pilih fitur hiburan yang ingin digunakan:",
        reply_markup=reply_markup
    )