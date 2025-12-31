# Movie Recommendation System 

A Streamlit-based web application that suggests movies based on content similarity.

**Content-Based Filtering**: Uses a "soup" of features including Overview, Genres, Keywords, Cast, and Director.

## 🧠 Cara Kerja Sistem (Algorithm)

Sistem ini bekerja menggunakan metode **Content-Based Filtering**, di mana rekomendasi diberikan berdasarkan kemiripan atribut antar film. Berikut langkah-langkah utamanya:

1.  **Ekstraksi Fitur (Feature Extraction)**:
    *   Menggabungkan metadata film: **Overview**, **Genres**, **Keywords**, **Cast** (3 aktor utama), dan **Director**.
    *   **Pembersihan Nama**: Menghapus spasi pada nama (contoh: "Brad Pitt" $\rightarrow$ "BradPitt") agar menjadi satu token unik.

2.  **Feature Soup & Weighting**:
    *   Semua fitur digabungkan menjadi satu teks panjang yang disebut "soup".
    *   **Pembobotan (Weighting)**: Fitur penting seperti *Genres*, *Keywords*, *Cast*, dan *Director* diulang sebanyak **3x** untuk meningkatkan pengaruhnya dibandingkan *Overview*.
    *   *Formula*: $\text{Soup} = \text{Overview} + (3 \times \text{Genres}) + (3 \times \text{Keywords}) + (3 \times \text{Cast}) + (3 \times \text{Director})$

3.  **Vektorisasi (Vectorization)**:
    *   Sistem mengubah teks "soup" menjadi representasi angka (vektor) menggunakan **CountVectorizer**.
    *   Setiap film direpresentasikan sebagai sebuah titik dalam ruang multi-dimensi.

4.  **Perhitungan Kesamaan (Similarity Calculation)**:
    *   Sistem menghitung **Cosine Similarity** (Kesamaan Kosinus) antar vektor film.
    *   Semakin kecil sudut antar vektor, semakin mirip kedua film tersebut.
    *   Hasilnya adalah daftar film dengan skor kemiripan tertinggi yang disajikan ke pengguna.

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
