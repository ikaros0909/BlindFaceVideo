import speech_recognition as sr

r = sr.Recognizer()

# Set up the microphone
with sr.Microphone() as source:
    print("Speak now:")
    audio = r.listen(source)

# Transcribe the audio
text = r.recognize_google(audio)
print(text)