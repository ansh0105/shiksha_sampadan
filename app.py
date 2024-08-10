import os
import shutil
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_option_menu import option_menu
from PIL import Image
from chatbot.topic_explanatory import topic_explanatory 
import pygame

st.set_page_config(page_title="Sampadan",page_icon="📚",layout="wide")


def session_init():
    """
    To declare session vaiables of streamlit.
    1. handle_user_input_check (deafult: True)
    2. audio_check_flag (deafult: True)
    3. submit_flag (default: False) 
    4. new_topic_list (default: [])
    """
    if not hasattr(st.session_state,"handle_user_input_check"):
        st.session_state.handle_user_input_check = True

    if not hasattr(st.session_state,"audio_check_flag"):
        st.session_state.audio_check_flag = True

    if not hasattr(st.session_state,"submit_flag"):
        st.session_state.submit_flag = False

    if not hasattr(st.session_state,"new_topic_list"):
        st.session_state.new_topic_list = []


def pygame_manager_func():
    """
    To initialize and stop music
    """
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.quit()
    pygame.mixer.init()


def remove_create_audio_directory():
    """
    Check and remove directory audio_dir if exists and create empty directory
    """
    if os.path.exists("audio_dir"):
        shutil.rmtree("audio_dir")
    os.makedirs('audio_dir',exist_ok=True)


if __name__ == "__main__":
    
    pygame_manager_func()
    remove_create_audio_directory()
    session_init()

    st.markdown("""
            <style>
                .block-container {
                        padding-top: 2rem;
                        padding-bottom: 0rem;
                        padding-left: 2.5rem;
                        padding-right: 2.5rem;
                    } 
                
                .div.css-10qvep2.e1f1d6gn1 {
                height=10px !important;
                }
            </style>
            """, unsafe_allow_html=True)

    with st.container():
            col1,col2=st.columns([0.17,0.83],gap="small")
            with col1:
                logo_image = Image.open("./assets/logo.png")
                resized_logo = logo_image.resize((200, 165))

                logo_width, logo_height = resized_logo.size
                logo= st.image(resized_logo, use_column_width=False, output_format="auto", width=logo_width) 
            with col2:
                st.title(":blue[Shiksha Sampadan]")
                st.subheader(":blue[-GenAI powered content generator]")
                st.divider()

    with st.container():
        selected_nav= option_menu(
                menu_title=None,
                options=["Topic Tutor"],
                icons = ["file-earmark-person-fill"],
                menu_icon="cast",
                default_index=0,
                orientation="horizontal",
                styles={"container": {"padding": "0.5!important","width":"100% !important"}}
                    )
        if selected_nav == "Topic Tutor":
            topic_explanatory()
    
            

