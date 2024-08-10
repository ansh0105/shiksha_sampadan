import time
import streamlit as st
import pandas as pd
from chatbot.chatbot_utils.chatbot_helper import get_non_rtr_convo_chain
from chatbot.chatbot_utils.prompts import level1_prompt, level2_prompt, level3_prompt
from bhashini_utils.bhashini_main import speak
import pygame

language_dict= {
     "English":"en",
     "Hindi":"hi",
     "Kannada":"kn",
     "Bangala":"bn"
}

def check():
     """
     Reinitialize session variables handle_user_input_check and audio_check_flag as True
     """
     st.session_state.handle_user_input_check =True
     st.session_state.audio_check_flag = True


def handle_user_input(prompt :str) -> str:
     """
     Helps to fetch answer from conversational chain using prompt 
     """
     answer = st.session_state.explanatory_chain.predict(input = prompt.format(st.session_state.selected_course,
                                                                                st.session_state.selected_subtopic,
                                                                                st.session_state.selected_chapter))
     return answer



def topic_explanatory():
    """
    Streamlit utility used to add features that will
    1. Integrate Large Language Model to Generate answer
    2. Integrate Bhashini 
    """
    df = pd.read_csv("assets/dummy_data.csv")
    uvalue =df["course_id"].unique()

    c_id_name_list=[]
    for unique_id in uvalue:
        c_id_name_list.append(f'{unique_id} : {df[ df["course_id"]==  unique_id]["course_name"].values[0]}')

    with st.container():
            col1,col2,col3=st.columns([0.33,0.33,0.33],gap="small")

            with col1:
                st.session_state.selected_course = st.selectbox('Select course:', c_id_name_list)
            with col2:
                st.session_state.c_id = st.session_state.selected_course.split(":")[0].strip()
                
                st.session_state.selected_chapter = st.selectbox('Select chapter:',
                                                                df[df["course_id"]== int(st.session_state.c_id)]["chapter"].values
                                                                )
            with col3:
                st.session_state.topic_list = df[df["course_id"]==int(st.session_state.c_id)]["subtopic"].values
                st.session_state.new_topic_list = []
                for t in st.session_state.topic_list:
                    for splited_text in t.split(","):
                        st.session_state.new_topic_list.append(splited_text)                          

                st.session_state.selected_subtopic = st.selectbox('Select topic:',st.session_state.new_topic_list)
    
    with st.container():
         column1,column2,column3 = st.columns([0.33,0.33,0.33],gap="medium")
         with column1:
             st.session_state.selected_level = st.selectbox("Selected Level:",
                                                            ("Level 1","Level 2","Level 3"))
         with column2:
             st.session_state.selected_language = st.selectbox("Select language:",
                                                            list(language_dict.keys())) 
         with column3:
              st.session_state.selected_audio = st.selectbox("Do you want audio?",
                                                            ["Yes","No"])
    st.session_state.submit_button = st.button("Submit",key ="b1", on_click=check)
    
    if st.session_state.submit_button or st.session_state.submit_flag:
        with st.status("Initializing Content Generation Process..........", expanded=True) as status:
            st.write("Retrieving content from knowledge base...")
            time.sleep(1)

            st.write("Initializing conversational chain...")
            st.session_state.explanatory_chain = get_non_rtr_convo_chain()

            st.write("Generating content...")
            if st.session_state.handle_user_input_check:
                if st.session_state.selected_level == "Level 1":
                    st.session_state.answer = handle_user_input(level1_prompt)
                elif st.session_state.selected_level == "Level 2":
                    st.session_state.answer = handle_user_input(level2_prompt)
                elif st.session_state.selected_level == "Level 3":
                    st.session_state.answer = handle_user_input(level3_prompt)

            st.write("Translating content...")
            st.session_state.answer = st.session_state.answer.replace("```", "")
    
            st.session_state.audio_file_path,st.session_state.translation_answer = speak(language_dict[st.session_state.selected_language],st.session_state.answer)
            st.session_state.handle_user_input_check = False
            
            st.write("Generating audio...")
            time.sleep(0.5)

            status.update(
                label="Process Complete!", state="complete", expanded=False
            )
            
        with st.container():
            st.markdown(st.session_state.translation_answer)
            st.session_state.submit_flag =True
            if st.session_state.audio_check_flag and st.session_state.selected_audio=="Yes":
                    st.session_state.audio_check_flag = False
                    pygame.mixer.music.load(st.session_state.audio_file_path)
                    pygame.mixer.music.play()
                    



         
         

    

        
                 

                 

