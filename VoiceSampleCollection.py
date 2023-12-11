import streamlit as st
from audiorecorder import audiorecorder

with st.form("my_form"):

   st.title("Audio Recorder")
   audio = audiorecorder("Click to record", "Click to stop recording")

   print(len(audio))

   st.form_submit_button('Submit')

st.write("Outside the form")