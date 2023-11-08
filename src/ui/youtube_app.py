import streamlit as st

def run_youtube_app():
   
    st.title("YouTube Link Processor")
    
    youtube_link = st.text_input("Enter a YouTube link:")

    if st.button("Submit"):
        if youtube_link:

            st.markdown(f"[Click here to open the video]({youtube_link})")
        else:
            st.warning("Please enter a valid YouTube link.")
