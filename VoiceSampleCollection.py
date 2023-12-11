import streamlit as st
from audiorecorder import audiorecorder

with st.form("my_form"):

   st.title("Audio Recorder")
   audio = audiorecorder("Click to record", "Click to stop recording")

   if len(audio) > 0:
       # To play audio in frontend:
       st.audio(audio.export().read())  

       # To save audio to a file, use pydub export method:
       audio.export("audio.wav", format="wav")

       # To get audio properties, use pydub AudioSegment properties:
       st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")

st.write("Outside the form")