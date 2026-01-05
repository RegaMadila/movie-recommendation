import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class ContentRecommender:
    def __init__(self):
        self.count = CountVectorizer(stop_words='english')
        self.cosine_sim = None
        self.indices = None
        self.df = None

    def fit(self, df):
        self.df = df
        
        # Create Count Matrix
        count_matrix = self.count.fit_transform(df['soup'])
    
        # Compute Cosine Similarity
        self.cosine_sim = cosine_similarity(count_matrix, count_matrix)
        
        self.indices = pd.Series(df.index, index=df['title']).drop_duplicates()
        
    def recommend(self, title, top_n=10):
        if self.indices is None:
            raise ValueError("Model not fitted")
            
        try:
            idx = self.indices[title]
        except KeyError:
            return ["Movie not found in database."]

        if isinstance(idx, pd.Series):
             idx = idx.iloc[0]

        sim_scores = list(enumerate(self.cosine_sim[idx]))

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[1:top_n+1]

        movie_indices = [i[0] for i in sim_scores]

        return self.df['title'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    data = {
        'title': ['Movie A', 'Movie B', 'Movie C'],
        'soup': ['action paramount tomcruise', 'romance love titanic', 'action paramount mission']
    }
    df = pd.DataFrame(data)
    rec = ContentRecommender()
    rec.fit(df)
    print("Recommendations for Movie A:", rec.recommend('Movie A', top_n=1))
