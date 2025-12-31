# Movie Recommendation System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)](https://streamlit.io/)

A Content-Based Movie Recommendation Engine built with Python and Streamlit. This application suggests personalized movie recommendations by analyzing metadata such as genres, keywords, cast, and directors using Cosine Similarity.

## Features

- **Content-Based Filtering**: Leverages a sophisticated "soup" algorithm combining metadata for accurate matching.
- **Weighted Logic**: Prioritizes `Genres`, `Keywords`, `Director`, and `Cast` over generic plot summaries.

## How It Works

The system recommends movies by finding ones that are scientifically similar to your favorites. Here's the simplified process:

1.  **Data Ingestion**: We aggregate movie data including **Description**, **Genre**, **Refined Keywords**, **Cast**, and **Director**.
2.  **Preprocessing**: We sanitize names (e.g., "Tom Cruise" $\rightarrow$ "TomCruise") to create unique entity tokens.
3.  **Feature "Soup"**: We combine all attributes into a single text vector.
    *   *Weighting*: **Genre**, **Cast**, and **Director** are repeated **3x** to increase their influence on the recommendation, ensuring stylistic matches over simple keyword matching.
4.  **Similarity Engine**:
    *   We convert the "soup" into numerical vectors using `CountVectorizer`.
    *   We calculate the **Cosine Similarity** between vectors. Small angles $\approx$ High Similarity!

## Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/RegaMadila/movie-recommendation.git
    cd movie-recommendation
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
## Usage

Run the web application:
```bash
streamlit run app.py
```