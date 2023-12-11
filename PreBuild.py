import os
import pyaudio
import speech_recognition as sr
import pyttsx3
import pyglet

def recognizeSpeech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-то:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + text)
        return text
    except sr.UnknownValueError:
        print("Ошибка распознования")
        return None
    except sr.RequestError:
        print("Ошибка")
        return None

def playSpeakAudio():
    mus = pyglet.resource.media("active.mp3")
    mus.play()

def playSuccessAudio():
    mus = pyglet.resource.media("success.mp3")
    mus.play()

def speakText(message):

    # Используем воспроизведение для Windows
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)

    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        recognized_text = recognizeSpeech()
        if (recognized_text == "Привет"):
            speakText("Слушаю")
            playSpeakAudio()
            recordTask = recognizeSpeech()

            if (recordTask):
                playSuccessAudio()
                speakText(recordTask)