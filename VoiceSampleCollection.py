import streamlit as st
#from audiorecorder import audiorecorder
#import audio_recorder_streamlit as ars
import streamlit_mic_recorder as smr

with st.form("my_form"):

   st.title("Audio Recorder")
   audio_bytes = smr.mic_recorder(start_prompt="Start",stop_prompt="Stop")
   if audio_bytes:
       st.audio(audio_bytes['bytes'], format="audio/wav")

   submit_clicked = st.form_submit_button('Submit')

   if submit_clicked:
      print(len(audio_bytes))

st.write("Outside the form")