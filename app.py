# - CODE SETUP
import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Website", page_icon=":mountain:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")
# - MAIN CODE - #
# - THE INTRODUCTION SECTION - #
with st.container():

    # - TITLE - #
    st.subheader("Greetings Viewers, I'm...")
    st.title("TupperGamer90")
    st.header("[Check Out My YouTube Channel!](https://youtu.be/ivtte7E9Wso?si=fKnHUAmu-qnLvNta)")
    
# --- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Introduction")
        st.write("""
        - I sometimes code stuff when I'm not making videos on YouTube, such as making this Promotional Website. Which I made with Python
        - I try to create top-quality videos as well with my signature stuff in my 
        videos.
        - I have experience working on various projects, from social initiatives to sustainability.
        - My goal is to get people to Subscribe to my YouTube channel and people to watch my videos.
        - My Target for my channel is currently 100,000 (100k) Subscribers for my youtube channel
        - My dream is to buy something... I can't let you guys know what it is... but I hope I get enough money for it. It costs ~2,600,000 Rp.
        - Ah yes of course my 2nd dream is to run my YouTube channel.
            """)
        st.write("-")
        st.header("Channel Stats")
        st.write("""
        - Current Subscribers: 209
        - Channel Total views: 39k Views
        - Channel Verticication: Level 2
        - NOTE: Information might be outdated.""")
        st.write("-")
        st.write("Click below for my Youtube Channel!")
        st.header("[Click Here!](https://youtu.be/ivtte7E9Wso?si=fKnHUAmu-qnLvNta)")
    with right_column:
        st.image(Image.open(r"images\Pic.png"), width=400)

# - VIDEOS SECTION - #
# - VIDEO #1 - #
with st.container():
    st.write("---")
    st.header("- Videos Section -")
    st.write("##")
    left_section, right_section = st.columns((1, 2))
    with left_section:
        st.image(Image.open("images\ThumbnailOne.webp"), use_column_width=True)
    with right_section:
        st.subheader("Best Creations from the Scrap Mechanic Community! [PART 2]")
        st.write("""Hello guys today we have a part two to the showcasing video where we will showcase more creations! 
                 This video is about seeing what other people made online such as A Knock-Off Fromula 1 Car, and also a Crop Harvester.
        """
        )
        st.text("To Watch the Video:")
        st.markdown("[Click Here!](https://youtu.be/KB7oE0i3ZK4?feature=shared)")

# - VIDEO #2 - #
with st.container():
    left_section, right_section = st.columns((1, 2))
    with left_section:
        st.image(Image.open("images\ThumbnailTwo.webp"), use_column_width=True)
    with right_section:
        st.subheader("I Made Airplane wings FLEX In Kerbal Space Program!")
        st.write("""Hello, guys and Tupper is back! 
                 Today we're doing an interesting experiment where we make wings flex! 
                 Like and Subscribe and enjoy the video!
        """
        )
        st.text("To Watch the Video:")
        st.markdown("[Click Here!](https://youtu.be/ivtte7E9Wso?si=fKnHUAmu-qnLvNta)")

# - VIDEO #3 - #
with st.container():
    st.write("--")
    left_section, right_section = st.columns((1, 2))
    with left_section:
        st.image(Image.open("images\ThumbnailThree.webp"), use_column_width=True)
    with right_section:
        st.subheader("Scrap Mechanic 'Complex' Train Mechanics: My Most Complicated Train Part 2")
        st.write("""Tupper is back and today we'll see this train that somehow broke his recording software! 
                 This train has literally has FOUR Carts total, and it's in Simple 1 Physics Mode!
        """
        )
        st.text("To Watch the Video:")
        st.markdown("[Click Here!](https://youtu.be/ivtte7E9Wso?si=fKnHUAmu-qnLvNta)")
        

# - CHANNEL PREVIEW VIEW - #
with st.container():
    st.write("---")
    st.header("This is my Channel Page:")
    st.image(Image.open("images\Channel.png"), use_column_width=True)
    st.header("This is my Channel Details:")
    st.image(Image.open("images\Details.png"), use_column_width=True)

