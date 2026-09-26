import speech_recognition as sr
import webbrowser
import music
from gtts import gTTS
import pygame
import os

# Initialize pygame mixer only once
pygame.mixer.init()

# Text to Speech
def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("hello.mp3")

    pygame.mixer.music.load("hello.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("hello.mp3")


recognizer = sr.Recognizer()


def processcommand(c):
    print("Command:", c)

    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open music" in c.lower():
        speak("Opening Music")
        webbrowser.open("https://www.youtube.com/watch?v=tvcaYU7uofY&list=RDtvcaYU7uofY&start_radio=1")

    elif "open har bar" in c.lower():
        speak("Opening Har Bar")
        webbrowser.open("https://www.youtube.com/watch?v=XYmTfNiAqW8&list=RDtvcaYU7uofY&index=5")

    elif "open chat gpt" in c.lower():
      webbrowser.open("https://chat.openai.com")

    elif "open whatsapp" in c.lower():
     webbrowser.open("https://web.whatsapp.com")
   
    elif "open calculator" in c.lower():
        speak("Opening Calculator")
        os.system("calc")

    elif "open command prompt" in c.lower() or "open cmd" in c.lower():
        speak("Opening Command Prompt")
        os.system("start cmd")

    elif "open file explorer" in c.lower() or "open explorer" in c.lower():
        speak("Opening File Explorer")
        os.system("explorer")

    elif "open notepad" in c.lower():
        speak("Opening Notepad")
        os.system("notepad")

    elif "open paint" in c.lower():
        speak("Opening Paint")
        os.system("mspaint")

    elif "open vscode" in c.lower():
        speak("Opening Visual Studio Code")
        os.system("code")


    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ", 1)[1]
            link = music.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        except:
            speak("Song not found")

    else:
        speak("Command not found")


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        print("Recognizing...")

        try:
            with sr.Microphone() as source:

                print("Listening...")

                recognizer.adjust_for_ambient_noise(source, duration=0.5)

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=2
                )

            command = recognizer.recognize_google(audio)

            print("You said:", command)

            if "jarvis" in command.lower():

                speak("Yes")

                with sr.Microphone() as source:

                    print("Jarvis Active...")

                    recognizer.adjust_for_ambient_noise(source, duration=0.5)

                    audio = recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=5
                    )

                command = recognizer.recognize_google(audio)

                print("Command:", command)

                processcommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Speech Recognition Error: {e}")

        except Exception as e:
            print("Error:", e)