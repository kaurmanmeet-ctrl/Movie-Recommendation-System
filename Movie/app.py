import streamlit as st
import pandas as pd
import pickle
import joblib
import os

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")
st.markdown("Pick a movie and we'll suggest 5 similar ones!")

# ── Load Files Safely ────────────────────────────────────────
@st.cache_data
def load_data():
    with open('movies.pickle', 'rb') as f:
        movies = pickle.load(f)
     if not os.path.exists('similarity.joblib'):
        with st.spinner("Downloading similarity matrix..."):   
            gdown.download(
                'https://drive.google.com/uc?id=1wdFweA1l-ukhX5Q30Qn1xDtNmZiyMTX1',
                'similarity.joblib',
                quiet=False
       )
    similarity = joblib.load('similarity.joblib')
    return movies, similarity

try:
    movies, similarity = load_data()
    st.success("✅ Data loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading files: {e}")
    st.stop()

movie_names = movies['title'].values

# ── Recommend Function ───────────────────────────────────────
def recommend(name_movie):
    matches = movies[movies['title'] == name_movie]
    if matches.empty:
        return ["❌ Movie not found!"]
    
    movie_index = matches.index[0]
    recommendations = similarity[movie_index]
    movie_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# ── UI ───────────────────────────────────────────────────────
name_movie = st.selectbox("🎥 Select a Movie", movie_names)

if st.button("🔍 Recommend"):
    with st.spinner("Finding similar movies..."):
        results = recommend(name_movie)
    
    st.success("Here are your recommendations!")
    for idx, movie in enumerate(results, 1):
        st.markdown(f"**{idx}.** {movie}")