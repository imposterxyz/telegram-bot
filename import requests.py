import random
from telegram.ext import Updater, MessageHandler, Filters

# Define your bot token
BOT_TOKEN = '7136734359:AAFmtt1T0xK7uk4AW4_A-AdXl1qIuk3Npxg'

# Function to generate a random reply
def generate_reply():
    replies = [
        "Hello!",
        "How are you?",
        "Nice to meet you!",
        "I'm a bot!",
        "Have a great day!",
        "What's up?",
        "Good to see you!"
    ]
    return random.choice(replies)

# Function to handle messages
def message_handler(update, context):
    # Get the incoming message
    message = update.message

    # Generate a random reply
    reply = generate_reply()

    # Send the reply
    message.reply_text(reply)

def main():
    # Initialize the bot
    updater = Updater(BOT_TOKEN, use_context=True)

    # Add message handler
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
