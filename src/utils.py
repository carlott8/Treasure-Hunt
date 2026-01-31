
import json
import config
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
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        #rf"Ciao {user.mention_html()}! Siete pronti per iniziare la caccia al tesoro?",
        rf"Ciao {user.mention_html()}! Sei pronta ad iniziare la caccia al tesoro? Per vincere dovrai rispondere correttamente a 8 domande.",
        reply_markup=ForceReply(selective=True),
    )
    context.user_data['Name'] = user
    context.user_data['status'] = 0
    context.user_data['prev_ans'] = 'right'
    #user_dict[list] = generate_random_path(user_dict, steps)
    return 



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Avete a disposizione una sola chiamata di aiuto. Chiama xxxxxxxx per avere un indizio")



async def text_message(status, previous_answer):
    with open(config.questions_path, "r", encoding="utf-8") as f:
        questions = json.load(f)
    #answers= json.load(config.answers)
    if previous_answer == "wrong":
        ans = "Sbagliato, prova ancora"
        
    elif status == 1:
        ans = questions["d1"]
    elif status ==2: 
        ans = questions["d2"]
    elif status ==3: 
        ans = questions["d3"]
    elif status ==4: 
        ans = questions["d4"]
    elif status ==5: 
        ans = questions["d5"]
    elif status ==6: 
        ans = questions["d6"]
    elif status ==7: 
        ans = questions["d7"]
    elif status ==8: 
        ans = questions["d8"]
    elif status ==9: 
        ans = questions["final"]
        status=0
        previous_answer = 'right'

    return ans, previous_answer

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open(config.answers_path, "r", encoding="utf-8") as f:
        answers = json.load(f)
    status = context.user_data['status']
    previous_answer = context.user_data['prev_ans']
    
    if status == 1:
        #if update.message.text.lower() in ('3', 'tre'):
        if update.message.text.lower() in answers["r1"]:
            status += 1
            previous_answer = 'right'
        else:
            previous_answer = "wrong"

    elif status == 2:
        if update.message.text.lower() in answers["r2"]:
            status += 1
            previous_answer = 'right'
        else:
            previous_answer = "wrong"

    elif status == 3:
        if update.message.text.lower() in answers["r3"]:
            status += 1
            previous_answer = 'right'
        else:
            previous_answer = "wrong"

    elif status == 4:
        if update.message.text.lower() in answers["r4"]:
            status += 1
            previous_answer = 'right'
        else:
            previous_answer = "wrong"

    elif status == 5:
        if update.message.text.lower() in answers["r5"]:
            status += 1
            previous_answer = 'right'
        else:
            previous_answer = "wrong"

    elif status == 6:
        if update.message.text.lower() in answers["r6"]:
            status += 1
            previous_answer = 'right'
        else:
            previous_answer = "wrong"

    elif status == 7:
        if update.message.text.lower() in answers["r7"]:
            status += 1
            previous_answer = 'right'
        else:
            previous_answer = "wrong"

    elif status == 8:
        if update.message.text.lower() in answers["r8"]:
            status += 1
            previous_answer = 'right'
        else:
            previous_answer = "wrong"
    
    elif status == 0: 
        status = status +1
        previous_answer = 'right'

    # salva SEMPRE lo stato
    context.user_data['status'] = status
    context.user_data['prev_ans'] = previous_answer

    text, previous_answer = await text_message(status, previous_answer)
    await update.message.reply_text(text)
