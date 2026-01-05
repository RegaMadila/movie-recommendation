import pandas as pd
import numpy as np
import kagglehub
import ast

def load_data():
    print("Downloading/Loading dataset from KaggleHub...")
    path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
    
    # Load the datasets
    movies = pd.read_csv(f"{path}/tmdb_5000_movies.csv")
    credits = pd.read_csv(f"{path}/tmdb_5000_credits.csv")
    
    return movies, credits

def _convert(obj):
    """Extracts 'name' from a JSON list object."""
    L = []
    try:
        for i in ast.literal_eval(obj):
            L.append(i['name'])
        return L
    except (ValueError, TypeError):
        return []

def _convert3(obj):
    """Extracts the top 3 'name' keys from a JSON list object."""
    L = []
    counter = 0
    try:
        for i in ast.literal_eval(obj):
            if counter != 3:
                L.append(i['name'])
                counter += 1
            else:
                break
        return L
    except (ValueError, TypeError):
        return []

def _fetch_director(obj):
    """Extracts the director's name from the crew list"""
    L = []
    try:
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
        return L
    except (ValueError, TypeError):
        return []

def _collapse(L):
    """Removes spaces from strings"""
    L1 = []
    for i in L:
        L1.append(i.replace(" ", ""))
    return L1

def prepare_data(movies, credits):
    """
    Merges and processes the movies and credits dataframes to create a 'soup' for recommendation.
    """
    print("Processing and merging data...")
    
    movies = movies.merge(credits, on='title')
    
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
    
    movies.dropna(subset=['overview'], inplace=True)
    
    for col in ['genres', 'keywords', 'cast', 'crew']:
        movies[col] = movies[col].fillna("[]")

    movies['genres'] = movies['genres'].apply(_convert)
    movies['keywords'] = movies['keywords'].apply(_convert)
    movies['cast'] = movies['cast'].apply(_convert3)
    movies['crew'] = movies['crew'].apply(_fetch_director)
    
    movies['genres'] = movies['genres'].apply(_collapse)
    movies['keywords'] = movies['keywords'].apply(_collapse)
    movies['cast'] = movies['cast'].apply(_collapse)
    movies['crew'] = movies['crew'].apply(_collapse)
    
    # Create the 'soup'
    movies['overview'] = movies['overview'].apply(lambda x: x.split())

    # Boost genres and keywords by repeating them 3x
    movies['genres'] = movies['genres'].apply(lambda x: (x * 3) if isinstance(x, list) else [])
    movies['keywords'] = movies['keywords'].apply(lambda x: (x * 3) if isinstance(x, list) else [])
    movies['cast'] = movies['cast'].apply(lambda x: (x * 3) if isinstance(x, list) else [])
    movies['crew'] = movies['crew'].apply(lambda x: (x * 3) if isinstance(x, list) else [])

    # Create tags by combining all lists
    movies['tags'] = movies.apply(lambda x: x['overview'] + x['genres'] + x['keywords'] + x['cast'] + x['crew'], axis=1)
    
    movies['soup'] = movies['tags'].apply(lambda x: " ".join(x))
    
    new_df = movies[['movie_id', 'title', 'soup']].copy()
    
    return new_df

if __name__ == "__main__":
    m, c = load_data()
    final_df = prepare_data(m, c)
    print(final_df.head())
    print("Data processing complete.")
