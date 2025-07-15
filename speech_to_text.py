import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file = "audio_sample.wav"

try:
    with sr.AudioFile(audio_file) as source:
        print("🎧 Listening to the audio...")
        audio_data = recognizer.record(source)
        print("🧠 Recognizing speech...")

        # Use Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        print("\n📄 Transcription:\n")
        print(text)

except FileNotFoundError:
    print("❌ Audio file not found. Make sure 'audio_sample.wav' is in the same folder.")
except sr.UnknownValueError:
    print("⚠️ Could not understand the audio.")
except sr.RequestError as e:
    print(f"❌ Could not request results from Google Speech Recognition service; {e}")
