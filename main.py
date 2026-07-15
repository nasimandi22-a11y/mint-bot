from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛒 Cek Stok",
                callback_data="cek_stok"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Selamat datang di Mint Mobile Store Distributor! 📱",
        reply_markup=reply_markup
    )


async def cek_stok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = """
📦 Mint Mobile Store

📊 STOK ITEM
✅ 11 Item Ready

💰 Harga:
📱 Mint Mobile — Rp 100.000
🌎 Mint Mobile + Roam — Rp 150.000

Silakan pilih produk:
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "📊 STOK ITEM",
                callback_data="stok_info"
            )
        ],
        [
            InlineKeyboardButton(
                "📱 Mint Mobile",
                callback_data="mint_mobile"
            ),
            InlineKeyboardButton(
                "🌎 Mint Mobile + Roam",
                callback_data="mint_roam"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text,
        reply_markup=reply_markup
    )


async def produk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "mint_mobile":
        text = """
📱 Mint Mobile

💰 Harga:
Rp 100.000

📊 Stok:
✅ 11 Item Ready

✅ Ready — Siap Order!
"""

    else:
        text = """
🌎 Mint Mobile + Roam

💰 Harga:
Rp 150.000

📊 Stok:
✅ 11 Item Ready

✅ Ready — Siap Order!
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "⬅️ Kembali",
                callback_data="cek_stok"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text,
        reply_markup=reply_markup
    )


async def stok_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = """
📊 STOK ITEM

📱 Mint Mobile
🌎 Mint Mobile + Roam

Total Stock:
✅ 11 Item Ready

💰 Harga:
📱 Mint Mobile — Rp 100.000
🌎 Mint Mobile + Roam — Rp 150.000
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "⬅️ Kembali",
                callback_data="cek_stok"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text,
        reply_markup=reply_markup
    )


app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler("start", start)
)


app.add_handler(
    CallbackQueryHandler(
        cek_stok,
        pattern="cek_stok"
    )
)


app.add_handler(
    CallbackQueryHandler(
        produk,
        pattern="mint_mobile|mint_roam"
    )
)


app.add_handler(
    CallbackQueryHandler(
        stok_info,
        pattern="stok_info"
    )
)


app.run_polling()
