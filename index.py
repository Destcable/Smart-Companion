import os
import pyaudio
import speech_recognition as sr
import pyttsx3

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

def speakText(message):

    # Используем воспроизведение для Windows
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)

    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    speakText("Слушаю")
    recognized_text = recognizeSpeech()

    if (recognized_text):
        speakText(recognized_text)
        pass
