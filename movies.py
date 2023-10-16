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
from style import *
st.set_page_config(page_title='RandomDB',layout='wide', page_icon="🎥")
https = PoolManager()
imdb = IMDB()  
style_buttons()  

base_url='https://www.movieposterdb.com/'
@st.cache_data
def get_data():
    try:

        return pd.read_feather('movies.feather')
    except:
        st.error('movie data not found')
movies=get_data()
placeholder=style_title()

genre=st.sidebar.selectbox("Genre", ("unspecified","Drama","Action", "Documentary", "Comedy","Adventure","Crime","Romance","Fantasy","Animation"
,"Mystery","Biography"))
language=st.sidebar.selectbox('Language', ('unspecified','Arabic','English','French','German',"Hindi","Italian",'Japanese','Korean','Spanish',"Turkish"))
#director=st.sidebar.selectbox('Director',["john","jake","ahmed"]) 
rating=st.sidebar.slider("minimal rating", min_value=1, step=1,max_value=10)
year=st.sidebar.slider('movie release year',min_value=1900,max_value=2019,value=(1950,2019))


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
                try:
                    st.write(ls1.iloc[pick]['description'])
                except:
                    st.write('no description available for this movie.')
 
    
    except(KeyError):
        
        col6.header(ls1.iloc[pick]['original_title']+' '+'('+str(ls1.iloc[pick]['year'])+')')
        col6.subheader("rated "+str(ls1.iloc[pick]['avg_vote'])+"/ 10")
        col6.image('https://c.tenor.com/YM3fW1y6f8MAAAAC/crying-cute.gif',caption='no poster found')

    except(IndexError):
        col5,col6,col7=st.columns([1,2,1])
        col6.image('megamind.png',caption="Try (unironically) lowering your expectations.")   
