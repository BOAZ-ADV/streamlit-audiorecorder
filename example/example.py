import streamlit as st
from audiorecorder import audiorecorder
import speech_recognition as sr

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())
    
    # To save audio to a file:
    wav_file = open("audio.wav", "wb")
    wav_file.write(audio.tobytes())

r = sr.Recognizer()


with wav_file as source:
    audio2 = r.record(source)


result = r.recognize_google(audio2, language = 'ko-KR', show_all=True)
print(result['alternative'][0]['transcript'])

text_output = st.empty()
text_output.markdown(f"**Text:** ")

