# Analisis Kualitas Kode & Kesiapan Portofolio ML

## Penilaian Objektif
**Status Saat Ini:** Belum sepenuhnya siap (Estimasi: 70-75% Ready).
Secara konsep dan struktur sudah di jalan yang benar, namun secara eksekusi teknis terdapat **bug fatal** dan beberapa praktik coding yang kurang standar untuk level profesional.

---

## 1. CRITICAL ISSUES (Prioritas Utama)
Masalah ini harus diperbaiki agar kode dapat berjalan dan dianggap valid.

### a. Fatal Bug di `src/data_processing.py`
Pada baris 100-113, kode logic pembuatan tags akan menyebabkan **Crash (`NameError`)**.
- **Masalah:** Variabel `tags` diisi menggunakan method `.append()`, tetapi list `tags` itu sendiri tidak pernah dideklarasikan/diinisialisasi sebelumnya.
- **Masalah Performa:** Penggunaan loop `for index, row in movies.iterrows():` untuk iterasi DataFrame adalah praktik buruk ("anti-pattern") di Pandas. Ini sangat lambat dibandingkan operasi vektor (*vectorized operations*).

**Solusi:**
Ganti logic loop `iterrows` dengan fungsi `.apply()` yang jauh lebih efisien dan pythonic.

---

## 2. Evaluasi Code Quality

| Aspek | Rating | Analisis Detail |
| :--- | :---: | :--- |
| **Modularitas** | ✅ Bagus | Struktur folder terpisah (`src/data_processing.py`, `src/recommender.py`, `app.py`) sangat baik. Memisahkan logika data, model, dan UI menunjukkan pemahaman *Software Engineering* yang solid. |
| **Object-Oriented** | ✅ Bagus | Penggunaan class `ContentRecommender` membuat kode lebih rapi, reusable, dan state-nya terjaga (dibandingkan sekadar kumpulan fungsi). |
| **Type Hinting** | ⚠️ Kurang | Tidak ada *Type Hints* (contoh: `def fit(self, df: pd.DataFrame) -> None`). Di level profesional, type hinting wajib untuk readability dan debugging. |
| **Dependency Mgmt** | ❌ Buruk | `requirements.txt` tidak memiliki versi spesifik (contoh: hanya tertulis `pandas`). Ini berbahaya karena update library di masa depan bisa mematahkan kodemu (breaking changes). Seharusnya: `pandas==2.2.0`. |
| **Efisiensi** | ⚠️ Kurang | Menghitung `cosine_similarity` untuk matriks N x N memakan memori kuadratik. Untuk 5000 data masih aman, tapi arsitektur ini tidak *scalable* untuk Big Data. Perlu dicatat saja sebagai pemahaman limitasi. |

---

## 3. Gap Menuju Standar Portofolio Profesional
Recruiter tidak hanya melihat hasil akhir, tapi juga **proses berpikir**. Kode saat ini terasa seperti hasil "Tutorial yang dirapikan".

### Kekurangan:
1.  **Tidak Ada Analisis Data (EDA):**
    - Portofolio ML tanpa Exploratory Data Analysis (EDA) terasa "buta". Kamu butuh Jupyter Notebook (`notebooks/analysis.ipynb`) yang menampilkan grafik distribusi genre, word clouds, analiss korelasi, dll.
2.  **Kurang Testing:**
    - Belum ada Unit Test. Menambahkan folder `tests/` dengan tes sederhana (misal: tes input kosong, tes karakter aneh) akan sangat meningkatkan nilai jualmu sebagai Engineer yang peduli kualitas.
3.  **Dokumentasi Teknis:**
    - `README.md` sudah oke, tapi bisa ditambahkan penjelasan mengenai keputusan teknis (kenapa bobot genre dikali 3? kenapa pakai Cosine Similarity?).

---

## 4. Action Plan (Rekomendasi Perbaikan)
1.  **Fix Logic Error:** Perbaiki bug `tags` di `data_processing.py` dan optimasi menggunakan `.apply()`.
2.  **Versioning:** Freeze versi library di `requirements.txt` (`pip freeze > requirements.txt`).
3.  **Type Hinting:** Tambahkan type hints di semua fungsi di folder `src/`.
4.  **Buat Notebook EDA:** Buat file notebook untuk analisis visual data sebelum masuk ke pemodelan.
