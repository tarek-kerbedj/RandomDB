import streamlit as st
def style_buttons():
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #000000;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #FF0000;
        color:##ff99ff;
        }
    </style>""", unsafe_allow_html=True)
    st.markdown("""
            <style>
                .css-18e3th9 {
                        padding-top: 0rem;
                        padding-bottom: 10rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
                .css-1d391kg {
                        padding-top: 3.5rem;
                        padding-right: 1rem;
                        padding-bottom: 3.5rem;
                        padding-left: 1rem;
                    }
            </style>
            """, unsafe_allow_html=True)
def style_title():
    st.markdown(""" <style text-align=center> .font {
    font-size:30px ; font-family: 'Brush Script MT', cursive; color: #ffffff;} 
    </style> """, unsafe_allow_html=True)
    #<div style="text-align: center"> your-text-here </div>
    #st.markdown('<p class="font" ,>IMDB Movies</p>', unsafe_allow_html=True)
    placeholder = st.empty()
    placeholder.markdown("<h1 style='text-align: center; color: white;'>&#127902;&#65039 IMDB randomizer &#127902;&#65039 </h1>", unsafe_allow_html=True)
    return placeholder