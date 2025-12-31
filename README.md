# Movie Recommender Portfolio Project

A Streamlit-based web application that suggests movies based on content similarity.

## Features
- **Content-Based Filtering**: Uses a "soup" of features including Overview, Genres, Keywords, Cast, and Director.
- **Interactive UI**: Built with Streamlit for easy exploration.
- **Modular Code**: Separated into data loading, processing, and recommendation logic.

## Setup
1. Unzip the project.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Key Technologies
- **Python**: Core language
- **Pandas**: Data manipulation
- **Scikit-learn**: TF-IDF/Count Vectorizer & Cosine Similarity
- **Streamlit**: Web Interface
