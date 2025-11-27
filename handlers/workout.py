from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def show_workout_menu(query, context):
    keyboard = [
        [InlineKeyboardButton("🏋️‍♂️ Workout Plan", callback_data="workout_plan")],
        [InlineKeyboardButton("💪 Exercise Demo", callback_data="exercise_demo")],
        [InlineKeyboardButton("📊 Progress Tracker", callback_data="progress_tracker")],
        [InlineKeyboardButton("🍽️ Diet Recommendation", callback_data="diet_recommendation")],
        [InlineKeyboardButton("⏱️ Timer Workout", callback_data="timer_workout")],
        [InlineKeyboardButton("🎯 Target Harian", callback_data="daily_target")],
        [InlineKeyboardButton("📈 BMI Calculator", callback_data="bmi_calculator")],
        [InlineKeyboardButton("💧 Water Reminder", callback_data="water_reminder")],
        [InlineKeyboardButton("🛌 Rest Timer", callback_data="rest_timer")],
        [InlineKeyboardButton("📚 Tips Workout", callback_data="workout_tips")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "💪 **Fitur Anak Workout**\n\n"
        "Pilih fitur workout yang Anda butuhkan:",
        reply_markup=reply_markup
    )