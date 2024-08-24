import pyttsx3
speech = pyttsx3.init()
speech.setProperty('rate', 150)
speech.setProperty('volume', 0.7)

def test():
    speech.say('Hello, I will check if your DNS address is valid or not')
    number = input("\033[1;32mEnter Your DNS address: ")
   

    if 0 <= int(number) <= 9999:
        print('Your DNS address is valid')
        speech.say('is a valid DNS address')
        speech.say('Thank you for using  Wolf software')
    else:
        print('Your DNS address is not valid')
        speech.say('is not a valid DNS address')
        speech.say('Thank you for using  Wolf software')

     
test()
speech.runAndWait()