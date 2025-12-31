# Movie Recommendation System 

A Streamlit-based web application that suggests movies based on content similarity.

**Content-Based Filtering**: Uses a "soup" of features including Overview, Genres, Keywords, Cast, and Director.

## 🧠 How It Works

The system recommends movies by finding ones that are similar to what you like. Here's the simple process:

1.  **Gather Info**: We take the movie's **Description**, **Genre**, **Refined Keywords**, **Cast**, and **Director**.
2.  **Clean Names**: We stick names together (e.g., "Tom Cruise" becomes "TomCruise") so the system knows it's one unique person.
3.  **Create a "Soup"**: We mix all this info into one big text called a "soup".
    *   *Important Stuff*: We repeat the **Genre**, **Cast**, and **Director** 3 times so they matter more than just the description.
4.  **Find Matches**: The system compares the "soup" of every movie.
    *   It uses math (Cosine Similarity) to see how close two movies are.
    *   If the angle between them is small, the movies are very similar!

## Setup
1. Unzip the project.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Structure
- `app.py`: Main Streamlit application.
- `src/`: Core logic modules.
  - `data_processing.py`: Data loading, cleaning, soup creation, and weighting.
  - `recommender.py`: Vectorization and cosine similarity logic.
- `algorithm_flow.md`: Detailed technical explanation of the algorithm.
