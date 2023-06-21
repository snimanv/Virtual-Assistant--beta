#importing necessary packages
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser

listener = sr.Recognizer() #Recognising your voice
engine = pyttsx3.init()  
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) #changing the voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source: 
            #talk('Hi! I am your personal virtual assistant beta.')
            #talk('how can i help you?')
            talk('Please give your command')
            print('listening.....')
            voice = listener.listen(source) #listening to the source
            command = listener.recognize_google(voice, language = "en-IN")
            command = command.lower()
            print(command)
            if 'beta' in command:
                command = command.replace('beta', '')
            
            
    except sr.UnknownValueError:
        talk("Sorry! I couldn't understand that")
        print("Unknown Value Error occurred")
        talk("Please try again later")
        print("Please try again later!!")
        return None
        
    except sr.RequestError:
        talk("Sorry! My speech recognition service is currently unavailable")
        print("Request Error occurred")
        talk("Please try again later")
        sys.exit()
    return command
    
def run_beta():
    while True:
        command = take_command()
        #print(command)
        if command is None:
            sys.exit()
            
    if 'stop' in command:
        sys.exit()
    
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The Current time is ' + time)
        
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'joke' in command:
        joke = (pyjokes.get_joke())
        print(joke)
        talk(joke)
        
    elif 'open' in command:
        sites = [["youtube", "https://www.youtube.com/"], ["wikipedia", "https://www.wikipedia.org/"], ["google", "https://www.google.com/"], ["instagram", "https://www.instagram.com/"], ["google map", "https://www.google.com/maps"]]
        site = command.replace('open', '').strip()
    
        for s in sites:
            if site in s[0]:
                talk("Opening the browser")
                webbrowser.open(s[1])
                break
                
        else:
            talk("Sorry, I couldn't find that site.")
        
        
    else:
        talk('Please say that command again.')

talk('Hi! I am your personal virtual assistant beta.')
while True:    
    run_beta()
