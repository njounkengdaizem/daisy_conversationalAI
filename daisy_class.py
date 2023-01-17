import os
import sys
import speech_recognition as speech
import pyttsx3
import pywhatkit
from datetime import date
import time
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Controller
import datetime
import wikipedia
import pyjokes

class Daisy():
    """
    Daisy is a class that provides a simple interface to interact with the user using speech recognition and Text-to-Speech. 
    The class uses several libraries such as speech_recognition, pyttsx3, pywhatkit, datetime, time, pynput, wikipedia, pyjokes.
    """

    def __init__(self) -> None:
        """
        The constructor method that initializes the listener, engine, and voices properties when an instance of the class is created.
        """
        self.listener = speech.Recognizer()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        for voice in self.voices:
            self.engine.setProperty('voice', voice.id)
            self.engine.setProperty('voice', self.voices[1].id)

    def talk(self,text):
        """
        This method takes a single argument, a text string, and uses the `pyttsx3` library to speak the text.
        """
        self.engine.say(text) 
        self.engine.runAndWait()

    def take_command(self):
        """
        This method listens to the microphone and uses the Google Speech Recognition service to recognize the audio.
        If the audio is not understood, it returns an empty string.
        """
        try:
            with speech.Microphone() as source:
                print('listening...')
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()
                if 'daisy' in command:
                    command = command.replace('daisy', '')
                    print(command)
        except speech.UnknownValueError as e:
            print("Could not understand audio")
            command = ""
        except speech.RequestError as e:
            print("Could not request from Google Speech Recognition service; {0}".format(e))
            command = ""
        return command

    def send_whatsapp_message(self, name:str):
        """
        This method takes a single argument, a name, and uses the `pywhatkit` library to send a WhatsApp message to the number associated with the given name.
        """
        for i in name:
            print (i)
            print("\n.")
        if "john" in name:
            pywhatkit.sendwhatmsg_instantly("+1(000)000-0000", "Howdy, como estas?")

    def send_whatsapp_image(self, phone_number:str, image:str):
        """
        This method takes two arguments, phone number and image, and uses the `pywhatkit` library to send a WhatsApp image to the given phone number.
        """
        pywhatkit.sendwhats_image(phone_number, image)

    def play_media(self, media:str):
        """
        This method takes a single argument, media, and uses the `pywhatkit` library to play the media on youtube.
        """
        self.talk('playing ' + media)
        pywhatkit.playonyt(media)

    def current_time(self):
        """
        This method tells the current time using `datetime` library.
        """
        time = datetime.datetime.now().strftime('%I:%M %p')
        self.talk('Current time is ' + time)

    def send_message(self, phone_number:str):
        """
        This method takes phone number as an argument and uses `os` and `pynput` library to open message application and send message to the given phone number.
        """
        os.system("open -a Messages")
        keyboard = Controller()
        keyboard.type("Hi beautiful, how are you doing?")
        keyboard.press(Key.enter)
