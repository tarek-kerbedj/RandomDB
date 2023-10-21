import pandas as pd
import streamlit as st
import json
from PyMovieDb import IMDB
import random
from urllib3 import PoolManager
from bs4 import BeautifulSoup
from style import *
from utils import *
st.set_page_config(page_title='RandomDB', layout='wide', page_icon="🎥")

https = PoolManager()
imdb = imdb_api_call()
style_buttons()

base_url = 'https://www.movieposterdb.com/'

movies = get_data()
placeholder = style_title()

genre = st.sidebar.selectbox("Genre", ("unspecified", "Drama", "Action", "Documentary", "Comedy", "Adventure", "Crime", "Romance", "Fantasy", "Animation", "Mystery", "Biography"))
language = st.sidebar.selectbox('Language', ('unspecified', 'Arabic', 'English', 'French', 'German', "Hindi", "Italian", 'Japanese', 'Korean', 'Spanish', "Turkish"))
rating = st.sidebar.slider("minimal rating", min_value=1, step=1, max_value=10)
year = st.sidebar.slider('movie release year', min_value=1900, max_value=2019, value=(1950, 2019))

col1, col2, col3 = st.sidebar.columns([1, 1, 1])
col5, col6, col7 = st.columns([1, 3, 1])
random_pick = col2.button('Search')

if year:
    begin, end = year

if random_pick:
    begin, end = year
    filtered_movies=filter_movies(movies,genre,language,rating, year)
    pick = random.randint(0, filtered_movies.shape[0])

    try:
        placeholder.empty()
        imdb_id = base_url + filtered_movies.iloc[pick]['imdb_title_id']
        res = imdb.get_by_id(filtered_movies.iloc[pick]['imdb_title_id'].replace("-i", "tt"))
        im = json.loads(res)['poster']
        col6.header(filtered_movies.iloc[pick]['original_title'] + ' ' + '(' + str(filtered_movies.iloc[pick]['year']) + ')')
        col6.subheader("rated " + str(filtered_movies.iloc[pick]['avg_vote']) + "/ 10")
        col6.image(im)
        with st.expander("movie description"):
            try:
                st.write(filtered_movies.iloc[pick]['description'])
            except:
                st.write('no description available for this movie.')

    except KeyError:
        col6.header(filtered_movies.iloc[pick]['original_title'] + ' ' + '(' + str(filtered_movies.iloc[pick]['year']) + ')')
        col6.subheader("rated " + str(filtered_movies.iloc[pick]['avg_vote']) + "/ 10")
        col6.image('https://c.tenor.com/YM3fW1y6f8MAAAAC/crying-cute.gif', caption='no poster found')

    except IndexError:
        col5, col6, col7 = st.columns([1, 2, 1])
        col6.image('megamind.png', caption="Try (unironically) lowering your expectations.")
