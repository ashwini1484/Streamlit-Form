#import streamlit as st
#from audiorecorder import audiorecorder
#import audio_recorder_streamlit as ars
# import streamlit_mic_recorder as smr

# with st.form("my_form"):

#    st.title("Audio Recorder")
#    audio_bytes = smr.mic_recorder(start_prompt="Start",stop_prompt="Stop")
#    if audio_bytes:
#        st.audio(audio_bytes['bytes'], format="audio/wav")

#    submit_clicked = st.form_submit_button('Submit')

#    if submit_clicked:
#       print(len(audio_bytes))

# st.write("Outside the form")

import streamlit as st
from streamlit_audio_recorder import st_audiorec

def main():
    st.title("Audio Recorder with Streamlit")

    audio_recording = st_audiorec()

    if st.button("Start Recording"):
        audio_recording.start()

    if st.button("Stop Recording"):
        audio_recording.stop()
        st.audio(audio_recording.get_audio(), format="audio/wav")

if __name__ == "__main__":
    with st.form("my_form"):
      main()

    st.write("Outside the form")