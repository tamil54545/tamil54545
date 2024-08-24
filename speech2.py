import pyttsx3
speech = pyttsx3.init()
'''''''''''''''
if (speech == None):
 print("Could not initialize speech engine")
else:
 speech.say('Sorry  please sppeching your speech')
language = 'ta'

speech.setProperty('rate', 130)
speech.setProperty('volume', 0.9)
speech.runAndWait()  
'''''''''''''''
speech.setProperty('rate', 150)
speech.setProperty('volume', 0.7)

otp = int(input('\033[1;32mEnter The  OTP : '))
#the volume of otp
speech.say(otp)


#They for Voice ID printing purposes & Language ID printing
''''''''''
voices = speech.getProperty('voices')
for voice in voices:
 print(voice, voice.id)
 speech.setProperty('voice', voice.id)
 '''''
if otp > 1000 :
   
   speech.say('success for Otp')
else:
    speech.say('please enter four Digits otp ')
    print("The Only For Four Digits OTP's")
if(speech ==None):
    print("Not showing for Number ")
    speech.say('Northing')


speech.runAndWait()
speech.stop()