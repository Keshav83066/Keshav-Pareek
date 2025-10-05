# chatbot 
# using numpy

import numpy as np
questions = np.array(["hello",
                      "hii",
                      "hey",
                      "what is your name?",
                      "how are you!",
                      "who are you",
                      "bye!"])

answers = np.array(["hello dear😊, how can I help you",
                    "hii , how can I help you",
                    "hey, whats going on today😊",
                    "my name is chatbot",
                    "I'm fine, whats you",
                    "I'm an openAi tool, and my name is chatbot",
                    "bye dear!😊"])

user_input = np.array(["stop",
                       "EXit",
                       "quite"])

while True:
    user_input = input("you : ").lower()
    
    found = False
    
    for i in range(len(questions)):
        if questions[i] in user_input or user_input in questions[i]:
            print("Bot : ", answers[i])
            found = True
            break
    
    if not found:      
        print("Bot: Sorry! I couldn't find the answer to that.")
        print("🔍 You can search your query here:")
        print("Google:", "https://www.google.com/search?q=" + user_input.replace(" ", "+"))
        print("ChatGPT:", "https://chat.openai.com")
 
