# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:29:44 2021

@author: LeviYagami76105
"""

import pyttsx3
from datetime import datetime
import speech_recognition as sr
engine = pyttsx3.init()
#engine.say("Hey KIRAN")
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Hello sai , Feeling cold? , me too ")


def time():
    time = datetime.now().strftime("%I:%M::%S")
    speak(time)
time()

def date():
    year = int(datetime.now().year)
    month = int(datetime.now().month)
    date = int(datetime.now().day)
    speak("current date is")
    speak(date)
    speak(month)
    speak(year)
#date()

def wish():
    speak("Hola!,Welcome back sir,How was your day?")
    #date()
    hour = datetime.now().hour
    if hour >=6 and hour <= 12:
        speak("Good Morning")
    elif hour >=12 and hour <16:
        speak("Good afn")
    elif hour >= 16 and hour < 19:
        speak("Good evening")
    else :
        speak("Good night")

    speak("Thursday at your service")
#wish()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio,'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again")
        return "None"
    return query
#takeCommand()
import wikipedia
import webbrowser as wb
import pyautogui



if __name__ == "__main__":
    wish()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching!, On your marks...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentence = 3)
            speak(result)    
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("You said me to remember"+remember.read())
        #elif "play a song" in query:
            #songs_dir = "song path"
            # songs = os.listdir(songs.dir)
            # os.startfile(os.path.join(songs_dir),songs[0])
             
    