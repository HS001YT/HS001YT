import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return ""
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = f"Searching Wikipedia for {person}"
        talk(info)
        pywhatkit.search(person)
    elif 'hello' in command:
        talk('Hi!')
    elif 'how are you doing' in command:
        talk('I am doing good! Thanks for asking!')
    elif 'bye' in command:
        talk('Goodbye!')
        exit()
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
