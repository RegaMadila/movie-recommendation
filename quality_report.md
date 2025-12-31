# Laporan Kualitas Rekomendasi Film

Berikut adalah analisis hasil pengujian otomatis terhadap 10 film acak menggunakan algoritma yang telah di-update (dengan bobot fitur yang ditingkatkan).

## Ringkasan Hasil
Dari 10 sampel film, sistem menunjukkan performa yang **sangat baik pada 40% kasus**, **cukup baik pada 30% kasus**, dan **kurang akurat pada 30% kasus**.

### ✅ Kategori Sukses Besar (Perfect Match)
Sistem sangat cerdas mengenali sekuel, genre spesifik, dan aktor utama.
1.  **Terminator 3** $\rightarrow$ Merekomendasikan *Terminator 1, 2, Salvation, Genisys*. (Sangat akurat karena bobot Keyword/Cast/Genre bekerja maksimal).
2.  **De-Lovely (Drama, Music)** $\rightarrow$ Merekomendasikan *Fame, High School Musical*. (Genre "Music" berhasil menjadi sinyal kuat).
3.  **Changing Lanes (Action, Thriller)** $\rightarrow$ Merekomendasikan *Snakes on a Plane* (Sama-sama dibintangi **Samuel L. Jackson** dan bergenre Action).
4.  **Win a Date with Tad Hamilton! (Romcom)** $\rightarrow$ Merekomendasikan *The Ugly Truth* (Romcom klasik).

### ⚠️ Kategori Melenceng (Miss-Match)
Masih ada beberapa anomali dimana "Overview" (sinopsis) mungkin memiliki kata-kata umum yang menipu algoritma.
1.  **The Sea Inside (Drama)** $\rightarrow$ Merekomendasikan *Impostor, Dreamcatcher (Sci-Fi/Horror)*.
    *   *Analisis*: Film ini bercerita tentang kelumpuhan/kematian. Kemungkinan kata-kata seperti "Life", "Die", "Body" di sinopsis bertabrakan dengan sinopsis film Sci-Fi/Thriller. Bobot Genre "Drama" kalah disini.
2.  **The Lost Boys (Horror, Comedy)** $\rightarrow$ Merekomendasikan *Walk the Line (Music/Biopic)*.
    *   *Analisis*: Ini aneh. Mungkin ada kesamaan di Keyword atau Crew yang tidak terlihat jelas, atau noise dari Overview.
3.  **In the Land of Women** $\rightarrow$ Merekomendasikan *Puss in Boots*.
    *   *Analisis*: Agak random.

## Kesimpulan Teknis
Strategi **"Feature Weighting" (Genre x3, Cast x3)** terbukti sangat efektif untuk film waralaba (Terminator) dan genre niche (Musik). Namun, untuk film Drama sosisal (The Sea Inside), sistem masih sering "terkecoh" oleh noise dari sinopsis.

**Rekomendasi Selanjutnya (Future Work):**
- Naikkan lagi bobot **Genre** menjadi 5x atau 10x untuk film non-franchise.
- Terapkan **Negative Weighting** untuk kata-kata umum di Overview (seperti "life", "one", "man").
