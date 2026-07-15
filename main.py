from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🛒 Cek Stok", callback_data='cek_stok')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selamat datang di Mint Mobile Store!", reply_markup=reply_markup)

async def cek_stok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer(10)
    await query.edit_message_text("Stok ready bro!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(cek_stok, pattern='cek_stok'))
app.run_polling()
