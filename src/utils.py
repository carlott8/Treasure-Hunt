

import logging
import random
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def generate_random_path(user_dict, steps):
    lst = list(range(steps+1)[1:])
    #print(lst)
    array_numbers = random.sample(lst, steps)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, user_dict, steps) -> dict[dict]:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Ciao {user.mention_html()}! Siete pronti per iniziare la caccia al tesoro?",
        reply_markup=ForceReply(selective=True),
    )
    if user_dict.empty():
        user_dict={{}}
    user_dict[user]['status'] = 1
    user_dict = generate_random_path(user_dict, steps)
    return user_dict



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Avete a disposizione una sola chiamata di aiuto. Chiama xxxxxxxx per avere un indizio")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def asnwer():
    check_user_status()
