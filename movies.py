import pandas as pd
import streamlit as st
import math
import json
from PyMovieDb import IMDB
import random
import numpy as np
from time import perf_counter
from urllib3 import PoolManager
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import os

st.set_page_config(page_title='RandomDB',layout='wide', page_icon="🎥")
https = PoolManager()
imdb = IMDB()    
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
base_url='https://www.movieposterdb.com/'

def get_data():
    return pd.read_csv('movies.csv',dtype={"year": "int16","duration":"int16","votes":"int32",'avg_vote':'float32'})
movies=get_data()
st.markdown(""" <style text-align=center> .font {
font-size:30px ; font-family: 'Brush Script MT', cursive; color: #ffffff;} 
</style> """, unsafe_allow_html=True)
#<div style="text-align: center"> your-text-here </div>
#st.markdown('<p class="font" ,>IMDB Movies</p>', unsafe_allow_html=True)
placeholder = st.empty()
placeholder.markdown("<h1 style='text-align: center; color: white;'>&#127902;&#65039 IMDB randomizer &#127902;&#65039 </h1>", unsafe_allow_html=True)
#st.markdown("""<p style="font-size:48px">
#&#128512; &#128516; &#128525;&#127909;
#</p>""",unsafe_allow_html=True)
genre=st.sidebar.selectbox("Genre", ("unspecified","Drama","Action", "Documentary", "Comedy","Adventure","Crime","Romance","Fantasy","Animation"
,"Mystery","Biography"))
language=st.sidebar.selectbox('Language', ('unspecified','Arabic','English','French','German',"Hindi","Italian",'Japanese','Korean','Spanish',"Turkish")) 
#director=st.sidebar.selectbox('Director',["john","jake","ahmed"]) 
rating=st.sidebar.slider("minimal rating", min_value=1, step=1,max_value=10)
year=st.sidebar.slider('movie release year',min_value=1900,max_value=2019,value=(1950,2019))
#actor=st.selectbox('Example',["john","jake","ahmed"])


#with st.sidebar.expander("Advanced options"):


col1, col2,col3= st.sidebar.columns([1,1,1])
col5,col6,col7=st.columns([1,3,1])
random_pick=col2.button('Search')


if year:
    begin,end=year

if random_pick:
    begin,end=year
    expr=movies[(movies['year']>begin) & (movies['year']<end) &(movies['avg_vote']>rating)]
    if language=='unspecified' and genre=='unspecified':
        ls1=expr
    elif language=='unspecified' and genre !='unspecified':
        ls1=expr[expr['genre'].str.match(genre)]
    elif language !='unspecified' and genre =='unspecified':
        ls1=expr[expr['language']==language]
    else:
         ls1=movies[(movies['year']>begin) & (movies['year']<end) &(movies['avg_vote']>rating) &(movies['language']==language)&(movies['genre'].str.match(genre)==True)]
   # st.subheader(ls1.shape[0])
    pick=random.randint(0,ls1.shape[0])
        #pick=random.randint(0,ls1.shape[0])
    
    try:
        placeholder.empty()
        imdb_id=base_url+ls1.iloc[pick]['imdb_title_id']    
        res = imdb.get_by_id(ls1.iloc[pick]['imdb_title_id'].replace("-i","tt"))
        im=json.loads(res)['poster']
        col6.header(ls1.iloc[pick]['original_title']+' '+'('+str(ls1.iloc[pick]['year'])+')')
        col6.subheader("rated "+str(ls1.iloc[pick]['avg_vote'])+"/ 10")
        col6.image(im)
        with st.expander("movie description"):

                st.write(ls1.iloc[pick]['description'])
    
    except(TypeError):
        #col6.image('https://c.tenor.com/yTEHRx1ofG4AAAAC/umaru-chan-tears.gif')
        
        col6.header(ls1.iloc[pick]['original_title']+' '+'('+str(ls1.iloc[pick]['year'])+')')
        col6.subheader("rated "+str(ls1.iloc[pick]['avg_vote'])+"/ 10")
        col6.image('https://c.tenor.com/YM3fW1y6f8MAAAAC/crying-cute.gif',caption='no poster found')

    except(IndexError):
        col5,col6,col7=st.columns([1,2,1])
        #col6.subheader('try lowering your expectations')
        #st.image('https://c.tenor.com/yTEHRx1ofG4AAAAC/umaru-chan-tears.gif')
        col6.image('megamind.png',caption="Try (unironically) lowering your expectations.")   
        #st.markdown("""<img src="megamind.png" style="width:100%;">""",unsafe_allow_html=True)
    #show title
   
    #show votes
   

    #show poster
 
