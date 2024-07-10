import os
from pydub import AudioSegment
import speech_recognition as sr

# Get the current directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script directory: {script_dir}")

# Path to the audio file (relative to the script directory)
audio_path = os.path.join(script_dir, 'media/recordings/voice002.m4a')
print(f"Audio file path: {audio_path}")

# Check if the audio file exists
if not os.path.exists(audio_path):
    print(f"Audio file not found: {audio_path}")
    exit(1)

# Convert .m4a to .wav for compatibility with speech recognition
try:
    audio = AudioSegment.from_file(audio_path, format="m4a")
    wav_path = os.path.join(script_dir, 'media/recordings/voice002.wav')
    audio.export(wav_path, format="wav")
    print(f"Converted WAV file path: {wav_path}")
except Exception as e:
    print(f"Error converting file: {e}")
    exit(1)

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Recognize the converted audio file
try:
    with sr.AudioFile(wav_path) as source:
        audio_text = r.record(source)
except Exception as e:
    print(f"Error reading audio file: {e}")
    exit(1)

# Use Google Web Speech API to transcribe the audio
try:
    transcription = r.recognize_google(audio_text)
    print("Transcription:")
    print(transcription)

    # Optionally save the transcription to a text file
    transcription_path = os.path.join(script_dir, 'media/transcriptions/transcription.txt')
    with open(transcription_path, "w") as file:
        file.write(transcription)
    print(f"Transcription saved to: {transcription_path}")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio")
