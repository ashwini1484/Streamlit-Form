import streamlit as st
from audiorecorder import audiorecorder

with st.form("my_form"):

   st.title("Audio Recorder")
   audio = audiorecorder("Click to record", "Click to stop recording")

   print(len(audio))

   submit_clicked = st.form_submit_button('Submit')

   if submit_clicked:
      print(len(audio))

st.write("Outside the form")