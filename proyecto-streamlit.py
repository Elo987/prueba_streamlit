#import openai
import streamlit as st
#import logging

from PIL import Image, ImageEnhance
import time
import json
import requests
import base64
#from openai import OpenAI, OpenAIError

img=Image.open("imgs/slogo.png")

st.set_page_config(
    page_title="Series temporales de acciones",
    page_icon=img,
    layout="wide",
    initial_sidebar_state="auto",

)


# Streamlit Title
st.title("Intraday liquidity series")

margins_css = """
    <style>
        .main > div {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 2rem;
        }
    </style>
"""

@st.cache_data(show_spinner=False)
def long_running_task(duration):
    """
    Simulates a long-running operation.

    Parameters:
    - duration: int, duration of the task in seconds

    Returns:
    - str: Completion message
    """
    time.sleep(duration)
    return "Long-running operation completed."





def display_streamlit_updates():
    """Display the latest updates of the Streamlit."""
    # with st.expander("Streamlit 1.36 Announcement", expanded=False):
    #     st.markdown("For more details on this version, check out the [Streamlit Forum post](https://docs.streamlit.io/library/changelog#version).")




def img_to_base64(image_path):
    """Convert image to base64."""
    with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()




def main():
    """
    Display Streamlit updates and handle the chat interface.
    """
    # initialize_session_state()

    # if not st.session_state.history:
    #     initial_bot_message = "Hello! How can I assist you with Streamlit today?"
    #     st.session_state.history.append({"role": "assistant", "content": initial_bot_message})
       

    # Insert custom CSS for glowing effect
    
    
    
    
    
    
    
    
    
    
    st.markdown(
        """
        <style>
        .cover-glow {
            width: 105%;
            height: auto;
            margin-top: -95px;

            position: relative;
            z-index: -1;
       
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
#     st.markdown("""
#   <style>
#     .css-o18uir.e16nr0p33 {
#       margin-top: -75px;
#     }
#   </style>
# """, unsafe_allow_html=True)

    # Load and display sidebar image


    #st.sidebar.markdown("---")

    # Load and display image with glowing effect
    img_path = "imgs/slogo.png"
    img_base64 = img_to_base64(img_path)
    
    
    import datetime
    import plotly.express as px
    df = px.data.stocks()
    
    
    
    
    
    
    
    if img_base64:
        st.markdown(margins_css, unsafe_allow_html=True)
        st.sidebar.markdown(
            f'<img src="data:image/png;base64,{img_base64}" class="cover-glow">',
            unsafe_allow_html=True,
            
        )
        
        
        with st.sidebar:
            st.title("Total liquidity from all counterparties")
            add_radio = st.radio(
                    "Choose granularity for forecasting:",
                    ("daily", "hourly")
            )
            
            predecir=st.button(label="forecast")
        
            st.text("--------------------------------")
            
            st.title("Show one counterparty")
        
            contrapartida=st.selectbox(label="Counterparty:", options=df.columns[1:])#["BBVA","BOFA","BNP"])
            
        
            add_calendar=st.date_input(label="Calendar:")
        
        
        fig = px.line(df, x='date', y=contrapartida, width=1500,color_discrete_sequence=["red"],)
        st.header("Valor de las acciones de " + contrapartida)
        st.plotly_chart(fig)

        st.header("Tabla de datos")
        st.dataframe(df,width=1500)
        
        
        
        
        
        
        
    
    


        # display_streamlit_updates()
main()