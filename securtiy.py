import wikipedia
import pyttsx3 as pytt

class ai:
    def __init__(self):
        self.engine = pytt.init()
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume', 0.9)
        print('Welcome to the  AI Assistant')
        self.engine.say('Welcome to the AI Assistant')
        self.engine.runAndWait()
        print("Hey Any Dots![ yes press(0)] or [no press(1)]")
        number =int(input('yes Press : '))
        if number == 0:
             self.engine.say('Okay! Please wait...')
             self.engine.say('Wow! Nice Topic')
             result =str(input('Enter your Dots? : '))
             self.engine.setProperty('rate', 125)
             self.engine.setProperty('volume', 0.9)
             sente = wikipedia.summary(result, sentences= 999)
             self.engine.say(sente)
             self.engine.runAndWait() 
        else:
            self.engine.say('No problem')
            self.engine.say('Okay!')
            self.engine.say('Goodbye')
            self.engine.runAndWait()

            

ai()



         

         


         

         


         