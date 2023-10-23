import random
from style import *
import json
from PyMovieDb import IMDB
import pandas as pd


@st.cache_data
def get_data():
    try:
        return pd.read_feather("movies.feather")
    except:
        st.error("movie data not found")


@st.cache_resource
def imdb_api_call():
    try:
        imdb = IMDB()
        return imdb
    except:
        st.error("failed to connect to the IMDB API")
        st.stop()


def filter_movies(movies, genre, language, rating, year):
    expr = movies[
        (movies["year"] > year[0])
        & (movies["year"] < year[1])
        & (movies["avg_vote"] > rating)
    ]
    if language == "unspecified" and genre == "unspecified":
        ls1 = expr
    elif language == "unspecified" and genre != "unspecified":
        ls1 = expr[expr["genre"].str.match(genre)]
    elif language != "unspecified" and genre == "unspecified":
        ls1 = expr[expr["language"] == language]
    else:
        ls1 = movies[
            (movies["year"] > year[0])
            & (movies["year"] < year[1])
            & (movies["avg_vote"] > rating)
            & (movies["language"] == language)
            & (movies["genre"].str.match(genre) == True)
        ]
    return ls1
