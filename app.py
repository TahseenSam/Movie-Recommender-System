import streamlit as st
import requests
import pickle
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=978cb90dac43d30cae107f64d2bc15ec&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index=movie_list[movie_list["title"]==movie].index[0]
    distances=sorted(enumerate(similarity[movie_index]),reverse=True,key=lambda x:x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movie_list.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movie_list.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

movie_list=pd.DataFrame(pickle.load(open("movie_dict.pkl","rb")))
similarity=pickle.load(open("similarity.pkl","rb"))


st.title("Movie Recommendation System")
movie_selected = st.selectbox(
    'Select a Movie?',
    movie_list["title"].values)

# st.write('You selected:', movie_selected)
if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(movie_selected)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
