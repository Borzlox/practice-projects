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
    elif 'who is the most pathetic creature' in command:
        talk('buzz the dog')
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
        talk('i am a dipshit computer')
    elif 'how are you doing' in command:
        talk('my disappointment is immeasurable and my day is ruined')
        talk('my life fucking sucks')
        talk('how about you?')
    elif 'why is my dog having diarhhea?' in command:
        talk('because he is a stupid fucking idiot')
    elif 'who is the stupidest dog' in command:
        talk('sully is a braindead mongrel')

run_jarvis()