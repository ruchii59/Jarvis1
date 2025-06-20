import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    tts_engine.say(text)
    tts_engine.runAndWait()

if __name__ == "__main__":
    speak("Hey sir, how may I help you?")

    # Use your Bluetooth mic by specifying device_index
    mic = sr.Microphone(device_index=2)  # Set this to your actual device index

    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening through Bluetooth mic...")
        audio = recognizer.listen(source, phrase_time_limit=5)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)

            if "open google" in command.lower():
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            else:
                speak("Sorry, I did not understand that command.")

        except sr.UnknownValueError:
            speak("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            speak("Could not request results; check your internet connection.")