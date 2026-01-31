from dotenv import load_dotenv
import os
load_dotenv() # save the variables in os


TOKEN = os.getenv("TOKEN_BOT")

questions_path = "C:\\Users\\Carlotta\\Desktop\\GIT\\Treasure-Hunt\\src\\questions.json"
answers_path = "C:\\Users\\Carlotta\\Desktop\\GIT\\Treasure-Hunt\\src\\answers.json"