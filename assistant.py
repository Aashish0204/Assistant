import webbrowser
import pyttsx3
import speech_recognition as sr
import os
from string import *
from datetime import datetime
from chat import use_chatbot
from database import *
import wolframalpha
import wikipedia

adict={}

class main_assistant:
    def __init__(self) :
        os.chdir("C:\\")
        self.find_exe("C:\\")
        os.chdir("A:\\")
        self.find_exe("A:\\")
        for x in adict.items():
            print(x)
        self.chatobj=use_chatbot()
        self.start()

    def start(self):
        self.listen()

    def call_wolframalpha(self,query):
        '''If this fucntion is called it will use the wolframalpha for getting answers of some questions'''
        app=wolframalpha.Client('LJQRRH-KWL23RXRXK')
        try:
            res=app.query(query)
            print(next(res.results).text)
            self.speak(next(res.results).text)
            return True
        except(Exception):
            print("passed")
            return False

    def call_wiki(self,query):
        '''If this is called then the response will be taken from wikipedia about it with 2 sentence only'''
        return(wikipedia.summary(query,sentences = 2))

    def speak(self,string):
        '''This function Speaks the string passed in it
        It Includes all the required properties for speaking.
        '''
        engine=pyttsx3.init()
        print(engine.getProperty('volume'))
        engine.setProperty('rate',150)
        engine.setProperty('volume',0.8)
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
        engine.say(string)
        engine.runAndWait()
        engine.stop()
        print(string)
        pass

    def greeting(self):
        '''This is a fucntion that greets the user accoding to the time using datatime module'''
        dt=datetime.now()
        curr_hr=dt.hour
        print(curr_hr)
        if(curr_hr>=5 and curr_hr<=12):
            self.speak("Good Morning")
        elif(curr_hr>=12 and curr_hr<=18):
            self.speak("Good Afternoon")
        elif(curr_hr>=18 and curr_hr<=24):
            self.speak("Good Evening")

    def find_exe(self,path):
        '''This is a fucntion that traverse through the path of c drive and
        a drive and stores all the exe files present in the Computer.It uses recursion and os module of python.
        '''
        # try:
        #     if(os.path.isdir(path)==True):
        #         os.chdir(path)
        #         templist=[]
        #         templist=(os.listdir())
        #         for i in range(0,len(templist)):
        #             temppath=os.path.join(path,templist[i])
        #             self.find_exe(temppath)
        #     elif ('.exe') in path:
        #         for i in range(len(path)-1,-1,-1):
        #             if(path[i]=='.'):
        #                 stop=i
        #             elif(path[i]=='\\'):
        #                 start=i
        #                 break
        #         value = path[slice(start+1,stop)].lower()
        #         adict[value]=path
        # except(Exception):
        #     pass

    def listen(self):
        '''This is a function that listens what user says from  the Microphone of computer
        and stores it in audio and using google recognition api it converts it into a string
        and calls the speak functions to speak it.
        '''
        self.greeting()
        while True:
            r=sr.Recognizer()
            with sr.Microphone() as src:
                print("Say..")
                audio=r.listen(src)
            try:
                print("Just a moment .. ")
                string=r.recognize_google(audio,language='en-in')
                string=string.lower()
                print(string)
                # self.speak(string)
                if 'exit' in string:
                    self.speak("Thank You ")
                    if(datetime.now().hour>=18 or datetime.now().hour<=5):
                        self.speak("Good Night")
                        break
                    else:
                        self.speak("Have a nice day")
                        break
                elif 'open youtube' in string:
                    webbrowser.open('www.youtube.com')
                elif 'open google'  in string:
                    webbrowser.open('www.google.com')
                elif 'open whatsapp web' in string:
                    webbrowser.open('web.whatsapp.com')
                elif 'open typeracer' in string:
                    webbrowser.open('www.typeracer.com')
                elif 'open cmd' in string:
                    os.startfile('cmd')
                elif 'your name' in string:
                    self.speak("My name is Assistant")
                    continue
                else:
                    pass
                myobj=open_command_db()
                openlist=myobj.get_opencmd_list()
                # print(openlist)
                for values in openlist:
                    print(values)
                    if(values in string):
                        templist=[]
                        templist=string.split()
                        templist.remove(values)
                        if('ms' in templist or 'my' in templist):
                            if('ms' in templist):
                                a=templist.index('ms')
                            elif('my' in templist):
                                a=templist.index('my')
                            templist[a]=templist[a]+templist[a+1]
                            templist.remove(templist[a+1])
                            print(templist)
                        for x in templist:
                            for y in adict.keys():
                                if(x in y):
                                    print("in if")
                                    templist=[]
                                    print(str(adict[x])+" is opened")
                                    os.startfile(adict[x])
                                    break
                    else:
                        print('passed from open')
                        pass
                myobj=close_command_db()
                closelist=myobj.get_closecmd_list()
                # print(closelist)
                for values in closelist:
                    print(values)
                    if(values in string):
                        templist=[]
                        templist=string.split()
                        templist.remove(values)
                        if('ms' in templist or 'my' in templist):
                            if('ms' in templist):
                                a=templist.index('ms')
                            elif('my' in templist):
                                a=templist.index('my')
                            templist[a]=templist[a]+templist[a+1]
                            templist.remove(templist[a+1])
                            print(templist)
                        for x in templist:
                            try:
                                os.system( "taskkill /im "+str(x)+str(".exe"))
                            except(Exception):
                                print("Task not found")
                                print("passed from close")
                                pass
                    else:
                        pass
                #parts remianing

                if(self.call_wolframalpha(string)):
                    continue
                else:
                    print("passed from wolfram")
                    pass
                try:
                    print(string)
                    response=self.chatobj.chatbot(string)
                    if(response==None):
                        pass
                    else:
                        self.speak(response)
                        print(response)
                        continue
                except Exception as e:
                    print("passed form chatterbot")
                    print(e)
                    pass
                try:
                    self.speak(self.call_wiki(string))
                except(Exception):
                    self.speak("Sorry Something went wrong")
                    print("passed from wiki")

            except Exception  as e :
                print(e)
                print("exception")
                continue
        self.listen()

obj=main_assistant()