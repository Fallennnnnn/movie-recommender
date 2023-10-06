# Laporan Proyek Machine Learning Movie Recommender System - Ega Fernanda Putra

## Project Overview

**Overview Proyek**

Proyek ini adalah pengembangan sistem rekomendasi film yang bertujuan untuk membantu penonton menemukan film-film yang sesuai dengan preferensi mereka dalam katalog film yang sangat besar dan beragam. Sistem rekomendasi ini akan memanfaatkan data film dari dataset TMDB Movies yang bersumber dari Kaggle. 

Industri film telah mengalami perkembangan yang pesat, dan penonton sekarang memiliki akses ke ribuan film dari berbagai genre, tahun rilis, dan negara. Kemudahan akses ini telah menciptakan tantangan baru dalam menavigasi dan menemukan film-film yang sesuai dengan selera pribadi. 

Pengembangan sistem rekomendasi film menjadi penting karena:
- **Penyederhanaan Pencarian**: Dalam tumpukan besar film, penonton sering kali kesulitan mencari film yang sesuai dengan selera mereka. Sistem rekomendasi dapat memfilter pilihan dan memberikan rekomendasi yang relevan.
- **Meningkatkan Kepuasan**: Rekomendasi yang akurat dapat meningkatkan pengalaman menonton film dan membuat penonton lebih puas dengan pilihan mereka.
- **Dukungan bagi Industri Film**: Film-film yang lebih kecil atau kurang dikenal juga dapat mendapatkan perhatian lebih dengan bantuan rekomendasi, yang mendukung pertumbuhan industri film secara keseluruhan.

## Business Understanding

Dalam bagian ini, akan dijelaskan potensi manfaat dari pengembangan sistem rekomendasi film dan bagaimana hal tersebut dapat meningkatkan pengalaman penonton serta mendukung industri film. Beberapa aspek yang akan dibahas adalah:

1. **Meningkatkan Pengalaman Menonton**: Sistem rekomendasi film dapat membantu penonton menemukan film-film yang lebih sesuai dengan preferensi mereka. Ini berpotensi meningkatkan kepuasan penonton, memastikan bahwa mereka menikmati film yang mereka tonton, dan mungkin menginspirasi mereka untuk mengeksplorasi genre atau film yang tidak mereka ketahui sebelumnya.

2. **Dukungan bagi Industri Film**: Film-film yang kurang dikenal atau berada di luar jangkauan perhatian utama juga dapat mendapatkan perhatian lebih dengan bantuan rekomendasi. Ini dapat mendukung pertumbuhan industri film secara keseluruhan dengan membantu film-film indie atau non-mainstream untuk ditemukan oleh khalayak yang lebih luas.

3. **Penyederhanaan Pencarian**: Dalam katalog film yang sangat besar dan beragam, penonton sering kali kesulitan mencari film yang sesuai dengan selera mereka. Sistem rekomendasi dapat memfilter pilihan dan memberikan rekomendasi yang relevan, menghemat waktu dan usaha penonton dalam pencarian.

4. **Pengembangan Platform Streaming**: Platform streaming film dapat meningkatkan daya tarik mereka dengan menyediakan rekomendasi yang lebih baik. Ini dapat membantu mereka menarik lebih banyak pelanggan dan meningkatkan retensi pengguna.

Pemahaman bisnis ini menjadi dasar untuk mengembangkan sistem rekomendasi film yang efektif, yang dapat memberikan nilai tambah kepada penonton dan industri film secara keseluruhan.

### Problem Statements

Dalam konteks pengembangan sistem rekomendasi film, berikut adalah pernyataan masalah yang perlu diatasi:

1. **Ketidakpastian dalam Preferensi Penonton**: Bagaimana mengatasi ketidakpastian dalam preferensi penonton? Penonton dapat memiliki selera film yang beragam, dan preferensi mereka dapat berubah seiring waktu. Bagaimana menghasilkan rekomendasi yang relevan dan menangani perubahan preferensi?

2. **Variabilitas dalam Data Film**: Data film yang tersedia memiliki berbagai atribut, seperti genre, aktor, sutradara, dan ulasan. Bagaimana mengintegrasikan atribut-atribut ini dengan baik untuk menghasilkan rekomendasi yang bervariasi dan sesuai?

3. **Cold Start Problem**: Bagaimana memberikan rekomendasi kepada penonton yang baru mendaftar atau belum memiliki riwayat menonton? Dalam konteks ini, bagaimana mengatasi masalah cold start untuk memastikan bahwa bahkan penonton baru dapat menikmati pengalaman menonton yang relevan?

### Goals

Dalam proyek ini, tujuan dari pernyataan masalah ini adalah:

1. **Mengembangkan Sistem Rekomendasi yang Akurat**: Mengembangkan sistem rekomendasi film yang dapat memberikan rekomendasi yang akurat kepada penonton berdasarkan preferensi mereka. Tujuan utama adalah meningkatkan kepuasan penonton dan membantu mereka menemukan film-film yang sesuai dengan selera mereka.

2. **Mengatasi Variabilitas Data Film**: Mengatasi variabilitas dalam data film dengan merancang algoritma yang dapat memanfaatkan berbagai atribut film, seperti genre, aktor, dan ulasan, untuk memberikan rekomendasi yang bervariasi.

3. **Menangani Cold Start Problem**: Mengembangkan strategi untuk menangani masalah cold start, yaitu memberikan rekomendasi kepada penonton baru atau yang belum memiliki riwayat menonton yang signifikan.

Dengan mencapai tujuan-tujuan ini, diharapkan dapat meningkatkan pengalaman menonton penonton, mendukung pertumbuhan industri film, dan membuat rekomendasi film menjadi lebih relevan dan efisien.

### Solution Approach

Dalam menghadapi pernyataan masalah yang telah dijelaskan sebelumnya, kami akan mengusulkan dua pendekatan berbeda untuk mengembangkan sistem rekomendasi film yang akurat dan relevan:

#### Pendekatan 1: Collaborative Filtering

1. **User-Based Collaborative Filtering**: Menggunakan metrik kesamaan penonton untuk merekomendasikan film berdasarkan perilaku serupa penonton.

2. **Item-Based Collaborative Filtering**: Menganalisis kesamaan antara film berdasarkan perilaku penonton yang sama.

#### Pendekatan 2: Content-Based Filtering

Menggunakan fitur-fitur film (genre, aktor, sutradara, ulasan) dan preferensi penonton untuk merekomendasikan film yang relevan.

Kombinasi kedua pendekatan ini akan membantu mengatasi ketidakpastian dalam preferensi penonton dan variabilitas dalam data film, dengan tujuan meningkatkan kepuasan penonton dan mendukung pertumbuhan industri film.

## Data Understanding
Dataset ini berisi berbagai atribut penting tentang film-film, termasuk informasi tentang tanggal rilis, judul, ringkasan, popularitas, jumlah suara, rata-rata peringkat, bahasa asli, genre, dan URL poster. Dengan atribut-atribut ini, dapat dikembangkan sistem rekomendasi film yang mempertimbangkan popularitas, peringkat, genre, dan bahasa asli untuk memberikan rekomendasi yang relevan kepada penonton.

Sumber Dataset:
- [Kaggle 9000+ Movies Dataset](https://www.kaggle.com/datasets/disham993/9000-movies-dataset/data).

Variabel-variabel pada Kaggle 9000+ Movies Dataset adalah sebagai berikut:

- Release_Date: Tanggal rilis film.
- Title: Nama film.
- Overview: Ringkasan singkat tentang film.
- Popularity: Metrik penting yang dihitung oleh pengembang TMDB berdasarkan jumlah tayangan per hari, suara per hari, jumlah pengguna yang menandainya sebagai "favorit" dan "watchlist," - - tanggal rilis, dan metrik lainnya.
- Vote_Count: Total suara yang diterima dari penonton.
- Vote_Average: Peringkat rata-rata berdasarkan jumlah suara dan jumlah penonton dalam skala 1 hingga 10.
- Original_Language: Bahasa asli film. Versi dubbing tidak dianggap sebagai bahasa asli.
- Genre: Kategori yang digunakan untuk mengklasifikasikan film.
- Poster_Url: URL poster film.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**Referensi**
- Roy, D., Dutta, M. A systematic review and research perspective on recommender systems. J Big Data 9, 59 (2022). (https://doi.org/10.1186/s40537-022-00592-5)
- Jayalakshmi S, Ganesh N, Čep R, Senthil Murugan J. Movie Recommender Systems: Concepts, Methods, Challenges, and Future Directions. Sensors (Basel). 2022 Jun 29;22(13):4904. doi: 
  10.3390/s22134904 PMID: 35808398; PMCID: PMC9269752. (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9269752/)
- S. Malik, “Movie Recommender System using Machine Learning”, EAI Endorsed Trans Creat Tech, vol. 9, no. 3, p. e3, Oct. 2022. (https://publications.eai.eu/index.php/ct/article/view/2712)

**---Ini adalah bagian akhir laporan---**
