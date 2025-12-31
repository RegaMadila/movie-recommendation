# Alur Kerja Algoritma Rekomendasi Film

Dokumen ini menjelaskan secara teknis bagaimana sistem memproses data mentah hingga menghasilkan rekomendasi film.

## 1. Data Ingestion (Pemuatan Data)
Proses dimulai di `src/data_processing.py`.
- **Input**: Dua file CSV dari dataset TMDB 5000.
    1.  `tmdb_5000_movies.csv`: Berisi metadata film (budget, overview, popularity, dll).
    2.  `tmdb_5000_credits.csv`: Berisi informasi kru dan aktor (cast, crew).
- **Proses**: Kedua file dimuat ke dalam *pandas DataFrame*.

## 2. Merging & Cleaning (Penggabungan & Pembersihan)
- **Merging**: Kedua DataFrame digabungkan (merge) berdasarkan kolom `id` film. Ini menyatukan informasi cerita (overview) dengan pemeran (cast).
- **Filtering**: Kita hanya mengambil kolom penting:
    - `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`.
- **Drop NA**: Baris yang tidak memiliki `overview` dihapus karena tidak bisa diproses.

## 3. Feature Extraction (Ekstraksi Fitur)
Data mentah di kolom seperti `genres` atau `cast` berbentuk JSON string (teks). Kita melakukan parsing untuk mengambil intinya:
- **Genres**: Mengambil semua nama genre (misal: `['Action', 'Adventure']`).
- **Keywords**: Mengambil semua kata kunci plot.
- **Cast**: Mengambil **3 aktor teratas** saja.
- **Crew**: Hanya mencari orang dengan jabatan `'job': 'Director'`.

## 4. Name Sanitization (Normalisasi Teks)
Ini adalah langkah krusial untuk akurasi.
- **Masalah**: Sistem komputer melihat "Sam Worthington" dan "Sam Mendes" memiliki kesamaan kata "Sam". Ini bisa bias.
- **Solusi**: Kita menghapus spasi.
    - "Sam Worthington" $\rightarrow$ `SamWorthington`
    - "Sam Mendes" $\rightarrow$ `SamMendes`
- **Hasil**: Sekarang `SamWorthington` adalah satu token unik yang berbeda total dengan `SamMendes`.

## 5. Creating the "Soup" (Pencampuran Fitur)
Kita menggabungkan semua atribut teks menjadi satu string panjang yang disebut **"soup"**.
$$ \text{soup} = \text{overview} + \text{genres} + \text{keywords} + \text{cast} + \text{director} $$
Contoh isi `soup`:
*"In the 22nd century a paraplegic marine... Action Adventure SciFi cultureclash future SamWorthington ZoeSaldana SigourneyWeaver JamesCameron"*

## 6. Vectorization (Vektorisasi)
Proses ini terjadi di `src/recommender.py` menggunakan `CountVectorizer`.
- **Tujuan**: Mengubah teks (soup) menjadi angka (vektor) agar bisa dihitung secara matematis.
- **Metode**: Setiap kata unik di seluruh 5000 film menjadi satu dimensi.
- **Hasil**: Matriks raksasa ukuran (4806 film x 30,000+ kata), berisi hitungan kemunculan kata.

## 7. Similarity Calculation (Perhitungan Kemiripan)
Kita menggunakan **Kosinus Kesamaan (Cosine Similarity)**.
- Kita mengukur sudut antara vektor setiap film.
- **Nilai 1.0**: Film identik (sudut 0 derajat).
- **Nilai 0.0**: Film tidak berhubungan sama sekali (tegak lurus).
- Hasilnya adalah matriks `cosine_sim` berukuran 4806x4806 yang menyimpan skor kemiripan antar setiap pasangan film.

## 8. Recommendation Logic (Logika Rekomendasi)
Saat user meminta rekomendasi untuk film "Avatar":
1.  Sistem mencari **index** dari "Avatar" di database.
2.  Sistem mengambil deretan skor kemiripan untuk index tersebut dari matriks `cosine_sim`.
3.  Skor diurutkan (Sort) dari tertinggi ke terendah.
4.  Sistem mengambil 10 film teratas (selain film itu sendiri).
5.  Sistem mengembalikan judul film tersebut sebagai output.
