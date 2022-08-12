from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

class teach_chatbot:
    def __init__(self):
        mychatbot=ChatBot('Assistant')
        conversation=['Hii',
        'Hello',
        "How are you",
        'I am fine , What about you']
        trainer = ListTrainer(mychatbot)
        trainer.train(conversation)
        while(True):
            asked=input()
            if(asked=='exit'):
                break
            else:
                response = mychatbot.get_response(asked)
                print(response)
            pass
        trainer.export_for_training('A:\\SEM4\\osl\\mini_project\\database_set\\taught.yml')

class use_chatbot:
    def __init__(self):
        self.mychatbot= ChatBot('Assistant')
        self.trainer = ChatterBotCorpusTrainer(self.mychatbot)
        self.temppath='A:\\SEM4\\osl\\mini_project\\database_set\\'

        for file in os.listdir(self.temppath):
            self.trainer.train(self.temppath + file)

    def chatbot(self,query):
        try:
            print("This is in chat",query)
            response = self.mychatbot.get_response(query)
            print(response)
            return(response)
        except(Exception):
            pass

# obj1=teach_chatbot()
# obj2=use_chatbot()