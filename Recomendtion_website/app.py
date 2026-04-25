import streamlit as st
import pandas as pd
import joblib

def recommend(movie_name):
    index_value = movies[movies['title']==movie_name].index[0]
    recommendation = similarities[index_value]
    values = sorted(enumerate(recommendation),key =lambda x : x[1],reverse= True)[0:6]
    result = []
    for i in values:
        val = i[0]
        result.append(movies['title'][val])
    return result[1:]

similarities = joblib.load("similarities.joblib",'rb')
movies = pd.read_csv('movies_name.csv')
movies.rename(columns={movies.columns[0] : 'index', movies.columns[1]: 'title'})
st.title("Movie Recomendation System ")
movie_name = st.selectbox(label="Select Movie You Liked ",options=movies['title'])
if st.button("Recommend"):
    st.header(f"The Recommended Movies Are : ")
    result = recommend(movie_name)
    for i in result:
        st.write(i)