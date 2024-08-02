import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()
    
    # Initialize the microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for speech...")
        
        # Capture the audio from the microphone
        audio = recognizer.listen(source)
        
        try:
            # Using google speech recognition
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized speech: {text}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service; check your network connection.")

if __name__ == "__main__":
    recognize_speech_from_mic()
