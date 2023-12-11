import streamlit as st
#from audiorecorder import audiorecorder
import audio_recorder_streamlit as ars

with st.form("my_form"):

   st.title("Audio Recorder")
   audio_bytes = audio_recorder()
   if audio_bytes:
       st.audio(audio_bytes, format="audio/wav")

   submit_clicked = st.form_submit_button('Submit')

   if submit_clicked:
      print(len(audio_bytes))

st.write("Outside the form")