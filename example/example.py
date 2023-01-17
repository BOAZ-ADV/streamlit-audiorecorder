import streamlit as st
from audiorecorder import audiorecorder
import STT
import time
# import speech_recognition as sr

st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())
    
    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())
    wav_file.close()

id = STT.BitoPost("audio.mp3")
time.sleep(5)
result = STT.BitoGet(id)


# r = sr.Recognizer()


# with wav_file as source:
#     audio2 = r.record(source)


# result = r.recognize_google(audio2, language = 'ko-KR', show_all=True)
# print(result['alternative'][0]['transcript'])

text_output = st.empty()
text_output.markdown(f"**Text:** {result}")

