from dotenv import load_dotenv
import os
load_dotenv() # save the variables in os


TOKEN = os.getenv("TOKEN_BOT")

questions_path = os.getenv("QUESTIONS_PATH")
answers_path = os.getenv("ANSWERS_PATH")


