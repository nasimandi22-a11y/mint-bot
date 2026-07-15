rom telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🛒 Cek Stok", callback_data='cek_stok')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🔥 Selamat Datang di Mint Mobile Store!\n\n"
        "Nikmati layanan digital premium dengan proses super cepat, aman, dan terpercaya ✨\n\n"
        "Tekan tombol di bawah untuk mulai order",
        reply_markup=reply_markup
    )

async def cek_stok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    text = """📦 Produk: Link Aktivasi Mint Mobile 90 Days
💰 Harga: Rp 150.000
📊 Stok: 11 item
✅ Ready — siap order!

Ketuk tombol di bawah untuk beli"""
    
    keyboard = [[InlineKeyboardButton("🛒 Beli Sekarang", callback_data='beli')]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

if name == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(cek_stok, pattern='cek_stok'))
    app.run_polling()
