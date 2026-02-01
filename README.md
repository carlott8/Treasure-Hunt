# Treasure-Hunt

The idea was to built a treasure hunt made of enigmas which didn't require physical movement around places (Well, at least for now), but only telegram to interact with the bot. 


Almost everything you need is in the src folder: 
1. Open telegram and create your own BOT with BOT FATHER. Save the token. 
2. Add your env file with the token bot. 
3. Create two json files, one with the questions and the other one with the answers. 
    Example of questions.json: { "d1": "Which is the capital of Denmark?", "d2": "...."}
4. Add the variables QUESTIONS_PATH and ANSWERS_PATH in your env file
5. run main.py

Please note that at the moment the bot is configured to have 8 questions. An alternative dynamic solution is commented in utils.py