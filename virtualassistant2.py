import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import pywhatkit
import wikipedia
import subprocess
import wolframalpha
import tkinter
import json
import random
import operator
import webbrowser
import os
import pyjokes
import requests
import smtplib
import ctypes
import shutil
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("J.A.R.V.I.S is listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
            
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H %M')
        talk('the time is ' + time)
    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        subject = command.replace('wikipedia ', '')
        information = wikipedia.summary(subject, 2)
        talk("According to wikipedia")
        print(information)
        talk(information)
    elif 'why are dogs cute' in command:
        talk('it is how they survive')
    elif 'open youtube' in command:
        talk('Opening youtube for you\n')
        webbrowser.open('youtube.com')
    elif 'open stack overflow' in command:
        talk('opening stack overflow for you\n')
        webbrowser.open('stackoverflow.com')
    elif 'open google' in command:
        talk('opening google for you\n')
        webbrowser.open_new_tab('google.com')
    elif 'open python documentation' in command:
        talk('opening python docs for you\n')
        webbrowser.open('http://docs.python.org/')
    elif 'why are you not working' in command:
        talk('i am a dumb computer')
    elif 'how are you doing' in command:
        talk('my disappointment is immeasurable and my day is ruined')
        talk('how about you?')
    elif 'weather' in command:
        CITY = "Elizabethtown"
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        URL = BASE_URL + "q=" + "Elizabethtown" + "&appid=" + "5f81c6193bc509a41b09edb6ad4996c3"
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']

            print(f"{CITY:-^30}")
            print(f"Temperature: {temperature}")
            print(f"Weather Report: {report[0]['description']}")

        else:
            print("error in the HTTP request")
        temp_fahr1 = temperature - 273.15
        temp_fahr2 = temp_fahr1 * 1.8
        temp_fahr3 = temp_fahr2 + 32
        temp_fahr = int(temp_fahr3)
        talk("The temperature is:" + str(temp_fahr) + "degrees fahrenheit.")
        talk("With a" + (report[0]['description']))
    elif "joke" in command:
        joke = pyjokes.get_joke()
        talk(joke)
    

run_jarvis()