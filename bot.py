import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🚗 خرید خودرو", "🚘 فروش خودرو"],
        ["🔍 جستجوی خودرو", "📞 ارتباط با ما"]
    ]

    await update.message.reply_text(
        "به ربات خودرو یاب تهران خوش آمدید 🚗\n\n"
        "چه خدمتی نیاز دارید؟",
        reply_markup=ReplyKeyboardMarkup(
            keyboard, resize_keyboard=True
        )
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به زودی این بخش فعال می‌شود. 🚗"
    )

def main():
    token = os.environ["BOT_TOKEN"]

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    app.run_polling()

if __name__ == "__main__":
    main()
