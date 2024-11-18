from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the token from BotFather
BOT_TOKEN = "YOUR_BOT_TOKEN"

# /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to **Ibdā'**!\n\n"
        "We specialize in generating creative and halal AI images. \n"
        "Use the following commands to interact with us:\n"
        "/generate_a_img - Create your own halal images.\n"
        "/contact_us - Get in touch with us directly.\n"
        "/channel - Join our official channel for updates."
    )

# /generate_a_img command (placeholder for now)
def generate_a_img(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Type your prompt after /generate_a_img. For example:\n"
        "`/generate_a_img A beautiful sunset over a mountain`"
    )

# /contact_us command
def contact_us(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Contact us on Telegram: @YourTelegramID")

# /channel command
def channel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Join our channel for updates: @YourChannelUsername")

# Main function to start the bot
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("generate_a_img", generate_a_img))
    dispatcher.add_handler(CommandHandler("contact_us", contact_us))
    dispatcher.add_handler(CommandHandler("channel", channel))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
