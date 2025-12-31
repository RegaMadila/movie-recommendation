import streamlit as st
import pandas as pd
from src.data_processing import load_data, prepare_data
from src.recommender import ContentRecommender

st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")

@st.cache_data
def get_data():
    with st.spinner('Downloading and processing data'):
        movies, credits = load_data()
        final_df = prepare_data(movies, credits)
    return final_df, movies 
@st.cache_resource
def get_model(df):
    model = ContentRecommender()
    model.fit(df)
    return model

def main():
    st.title("Movie Recommender System")
    st.markdown("""
    Welcome to the Content-Based Movie Recommender! 
    This app recommends movies based on shared features like **Genres**, **Keywords**, **Cast**, **Director**, and **Overview**.
    """)

    try:
        final_df, raw_movies = get_data()
        model = get_model(final_df)
        
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    # Sidebar
    st.sidebar.header("Recommendation Settings")
    selected_movie = st.sidebar.selectbox(
        "Choose a movie you like:",
        final_df['title'].values
    )
    
    num_recommendations = st.sidebar.slider("Number of recommendations:", 5, 20, 10)
    
    if st.sidebar.button("Recommend", type="primary"):
        recommendations = model.recommend(selected_movie, top_n=num_recommendations)
        
        st.subheader(f"Because you liked *{selected_movie}*:")
        
        # Display recommendations in a grid
        cols = st.columns(5)
        for i, movie_title in enumerate(recommendations):
            with cols[i % 5]:
                # Get basic info
                # In a real app we'd fetch posters from TMDB API, but for now just text
                st.info(movie_title)
                # Ensure we have the genre info to show
                # genre = raw_movies[raw_movies['title'] == movie_title]['genres'].values[0]
                # st.caption(f"Genres: {genre}")

    # About Section
    with st.expander("How does this work?"):
        st.write("""
        This system uses **Content-Based Filtering**. It builds a "soup" of metadata for each movie containing:
        - **Overview**: Plot summary
        - **Genres**: Action, Comedy, etc.
        - **Keywords**: Plot keywords
        - **Cast**: Top 3 actors
        - **Crew**: Director
        
        It then uses **CountVectorizer** to convert this text into numbers and calculates **Cosine Similarity** to find the closest matches to your selection.
        """)
        
if __name__ == "__main__":
    main()
