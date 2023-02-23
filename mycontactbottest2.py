import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! Please share your contact number with me.")
def contact(update, context):
    user_contact = update.message.contact
    context.bot.send_message(chat_id="5535073751", text=f"User {update.effective_user.username} ({update.effective_user.id}) shared their contact number: {user_contact.phone_number}")
def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that.")

    def main():
    # Create an instance of the Updater class
    updater = Updater(token="6193245860:AAEgPmE4OdMG2W8RZEi7A9itkJiShcCkFio", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for the commands and messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.contact, contact))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()
