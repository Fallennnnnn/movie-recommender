# Laporan Proyek Machine Learning Movie Recommender System - Ega Fernanda Putra

## Project Overview

**Overview Proyek**

Proyek ini adalah pengembangan sistem rekomendasi film yang bertujuan untuk membantu penonton menemukan film-film yang sesuai dengan preferensi mereka dalam katalog film yang sangat besar dan beragam. Sistem rekomendasi ini akan memanfaatkan data film dari dataset TMDB Movies yang bersumber dari Kaggle. 

Industri film telah mengalami perkembangan yang pesat, dan penonton sekarang memiliki akses ke ribuan film dari berbagai genre, tahun rilis, dan negara. Kemudahan akses ini telah menciptakan tantangan baru dalam menavigasi dan menemukan film-film yang sesuai dengan selera pribadi.(Roy, D., Dutta, M., 2022)

Pengembangan sistem rekomendasi film menjadi penting karena:
- **Penyederhanaan Pencarian**: Dalam tumpukan besar film, penonton sering kali kesulitan mencari film yang sesuai dengan selera mereka. Sistem rekomendasi dapat memfilter pilihan dan memberikan rekomendasi yang relevan. 
- **Meningkatkan Kepuasan**: Rekomendasi yang akurat dapat meningkatkan pengalaman menonton film dan membuat penonton lebih puas dengan pilihan mereka. 
- **Dukungan bagi Industri Film**: Film-film yang lebih kecil atau kurang dikenal juga dapat mendapatkan perhatian lebih dengan bantuan rekomendasi, yang mendukung pertumbuhan industri film secara keseluruhan. (Jayalakshmi S, Ganesh N, Čep R, Senthil Murugan J., 2022)

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

Dalam menghadapi pernyataan masalah yang telah dijelaskan sebelumnya, akan diusulkan dua pendekatan berbeda untuk mengembangkan sistem rekomendasi film yang akurat dan relevan:

#### Pendekatan 1: Content-Based Filtering

1. **Content-Based Recommendations**: Menganalisis fitur-fitur film (genre, aktor, sutradara, ulasan, dll.) untuk merekomendasikan film berdasarkan kesamaan atribut dengan film yang telah disukai oleh pengguna.

#### Pendekatan 2: Hybrid Recommendations

2. **Hybrid Recommendations**: Menggabungkan rekomendasi berdasarkan konten (Content-Based Filtering) dengan rekomendasi berdasarkan popularitas (Popularity-Based Recommendations) untuk memberikan rekomendasi film yang seimbang antara preferensi pengguna dan popularitas film.

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

Berikut ini adalah Visualisasi yang dilakukan untuk mendapatkan insight dari data yang telah diperoleh

1. **Distribution of Movie Ratings (Vote_Average):** Visualisasi ini mungkin dilakukan dengan membuat histogram atau diagram distribusi dari rating film (Vote_Average). Histogram ini akan memberikan gambaran tentang sebaran rating film dalam dataset. Insight yang bisa diperoleh adalah apakah mayoritas film memiliki rating yang tinggi, rendah, atau terdistribusi merata. Ini bisa memberikan gambaran awal tentang kualitas film dalam dataset.

2. **Ratings vs. Popularity:** Dalam visualisasi ini, Anda mungkin akan membuat scatter plot yang membandingkan rating film dengan popularitasnya. Ini akan membantu Anda memahami apakah ada korelasi antara rating yang tinggi dan popularitas film. Misalnya, Anda mungkin menemukan bahwa film dengan rating tinggi cenderung lebih populer, atau sebaliknya. Ini bisa membantu dalam pemahaman preferensi penonton.

3. **Distribution of Movie Genres:** Untuk visualisasi ini, Anda bisa membuat grafik batang atau pie chart yang menggambarkan sebaran genre film dalam dataset. Ini akan memberikan gambaran tentang genre yang paling banyak muncul dalam dataset. Mungkin Anda akan menemukan genre yang paling dominan dan genre yang jarang muncul. Ini bisa membantu Anda dalam pengelompokan dan analisis lebih lanjut berdasarkan genre.

4. **Visualize the Top-Rated Movies Based on Their Titles:** Visualisasi ini dapat berupa daftar film dengan rating tertinggi yang disajikan dalam bentuk tabel atau diagram batang horizontal. Hal ini akan membantu Anda mengidentifikasi film-film dengan rating tertinggi dan mungkin memperoleh wawasan tentang apa yang membuat film-film ini begitu populer.

5. **Movie Releases by Year and Month:** Anda dapat membuat visualisasi seperti grafik batang atau garis untuk menggambarkan jumlah rilis film per tahun dan per bulan. Ini akan memberikan pemahaman tentang tren perilisan film dari waktu ke waktu. Mungkin Anda akan menemukan bahwa ada tren tertentu dalam perilisan film yang berkaitan dengan musim atau tahun tertentu.
   
Berikut ini adalah hasil visualisasinya <br>
![rating](https://github.com/Fallennnnnn/movie-recommender/assets/84832657/07503ae5-51e0-4d2b-9500-f77e3adc947a) <br>
Dapat dilihat dari Gambar visualisasi rata rata rating dengan frekuensi tertinggi dari film berada pada 6 hingga 8 
![ratingvspop](https://github.com/Fallennnnnn/movie-recommender/assets/84832657/ce56c15c-14ea-49d7-8988-2d88ceba3163) <br>
Gambar tersebut menunjukkan scatter plot dari peringkat dan popularitas film. Peringkat adalah nilai dari 1 hingga 10 yang diberikan oleh pengguna untuk film tersebut, sedangkan popularitas adalah jumlah pengguna yang telah menonton film tersebut. Dari gambar tersebut, dapat dilihat bahwa terdapat hubungan positif antara peringkat dan popularitas. Artinya, film-film dengan peringkat yang lebih tinggi juga cenderung lebih populer.
![genres](https://github.com/Fallennnnnn/movie-recommender/assets/84832657/c42eb6d3-f133-46f9-95cf-d7461c4ecba5) <br>
Pada gambar diatas merupakan distribusi jumlah film berdasarkan genrenya dimana film dengan genre terbanyak adalah drama, comedy, dan action
![mostpop](https://github.com/Fallennnnnn/movie-recommender/assets/84832657/55bd81aa-1d46-4526-8217-0b763745d88d) <br>
Dapat dilihat pada gambar diatas film dengan popularitas tertinggi adalah **Spider Man No Way Home** disusul dengan **The Batman** dan **No Exit** 
![distribution](https://github.com/Fallennnnnn/movie-recommender/assets/84832657/be7b7c73-6164-4ef1-aec6-425065b66e3c) <br>
![distribution2](https://github.com/Fallennnnnn/movie-recommender/assets/84832657/15f16dfd-4700-4977-87b4-49e14341451b) <br>
Dapat dilihat pada visualisasi diatas adalah distribusi jumlah film berdasarkan waktu rilisnya dan film terbanyak rilis di tahun 2021 dan untuk bulan rilis teranyak pada bulan 10

Melalui tahapan EDA ini, Anda dapat memahami data dengan lebih baik, mengidentifikasi pola atau hubungan yang mungkin terjadi dalam dataset, dan mendapatkan wawasan awal yang berguna untuk analisis lebih lanjut.

## Data Preparation
Proses data preparation terkait dengan pengolahan data sebelum data tersebut siap untuk digunakan dalam analisis lebih lanjut. Berikut adalah langkah-langkah yang dilakukan : 

1. **Mengecek Data Kosong (Handling Missing Data):** Tahap pertama adalah memeriksa apakah ada data yang kosong (missing values) dalam dataset. Hal ini dilakukan dengan menggunakan perintah seperti `isnull()` atau `isna()` pada setiap kolom untuk mengidentifikasi baris yang memiliki data kosong. Data kosong dapat mengganggu analisis dan perlu diatasi. Pengguna dapat memutuskan apakah akan mengisi data yang kosong atau menghapus baris atau kolom yang memiliki data kosong, tergantung pada konteks dan banyaknya data yang hilang.

2. **Mengecek Duplikat (Handling Duplicate Data):** Setelah mengatasi data kosong, langkah berikutnya adalah memeriksa adanya duplikat dalam dataset. Duplikat dapat mengganggu analisis dan menghasilkan hasil yang bias. Gunakan perintah seperti `duplicated()` untuk mengidentifikasi dan menghapus baris yang merupakan duplikat dari data yang sudah ada.

3. **Mengecek Korelasi (Checking for Correlations):** Selanjutnya, perlu memeriksa korelasi antara variabel-variabel dalam dataset. Ini penting untuk memahami hubungan antara variabel dan mungkin untuk memilih hanya variabel yang paling relevan untuk analisis. Metode statistik seperti korelasi Pearson atau Spearman, serta visualisasi seperti matriks korelasi atau heatmap dapat digunakan.

4. **Drop Kolom Tidak Berguna (Dropping Unnecessary Columns):** Jika ada kolom-kolom dalam dataset yang tidak relevan untuk analisis atau tidak memiliki informasi yang berharga, dapat memutuskan untuk menghapus kolom-kolom ini. Ini akan membantu mengurangi dimensi data dan memudahkan analisis.

5. **Menggunakan Kolom "Genre" yang Dipisahkan oleh '|':** Jika kolom "Genre" dalam dataset berisi daftar genre yang dipisahkan oleh tanda '|', perlu melakukan pemrosesan tambahan untuk memisahkan genre-genre ini menjadi entitas terpisah. Metode seperti `str.split()` dapat digunakan untuk memisahkan genre-genre ini menjadi kolom-kolom baru atau menggabungkannya dengan cara yang sesuai dengan analisis.

6. **Menerapkan Pemrosesan Teks pada Kolom "Overview" untuk Menghasilkan Matriks TF-IDF:** Kolom "Overview" kemungkinan berisi teks deskripsi yang perlu diolah lebih lanjut sebelum dapat digunakan dalam analisis. Salah satu teknik yang umum digunakan adalah pemrosesan teks untuk menghasilkan matriks TF-IDF (Term Frequency-Inverse Document Frequency). Ini akan mengubah teks menjadi representasi numerik yang dapat digunakan dalam analisis data.

Setelah melalui langkah-langkah di atas, data akan siap untuk digunakan dalam analisis selanjutnya. Data preparation adalah langkah penting dalam proses analisis data karena membantu memastikan bahwa data yang digunakan adalah berkualitas dan sesuai dengan tujuan analisis yang dilakukan.

## Modeling
Dalam tahap Modeling, akan dijelaskan dua solusi rekomendasi yang digunakan dalam sistem rekomendasi film, yaitu Content-Based Filtering dan Hybrid Recommendations.

### Solusi 1: Content-Based Filtering

Solusi pertama adalah Content-Based Filtering, yang mengoperasikan rekomendasi berdasarkan kesamaan konten atau atribut film dengan film yang telah disukai oleh pengguna. Atribut konten yang digunakan dalam rekomendasi ini meliputi deskripsi film (Overview) dan genre film (Genres).

#### Cara Kerja Content-Based Filtering:
- Algoritma Content-Based Filtering menganalisis deskripsi film (Overview) dan genre film (Genres) yang telah disukai oleh pengguna.
- Selanjutnya, algoritma akan mencari film-film lain dalam dataset yang memiliki atribut konten serupa, seperti deskripsi atau genre yang mirip dengan film yang disukai oleh pengguna.
- Berdasarkan kesamaan ini, algoritma akan memberikan rekomendasi film yang memiliki atribut konten serupa dengan film yang telah disukai pengguna.

#### Kelebihan Content-Based Filtering:
- Mampu merekomendasikan film yang memiliki atribut konten serupa dengan film yang telah disukai pengguna.
- Tidak memerlukan informasi pengguna atau interaksi pengguna-film.

#### Kekurangan Content-Based Filtering:
- Cenderung membatasi variasi rekomendasi pada jenis film yang serupa dengan yang telah disukai pengguna.
- Tidak memperhitungkan popularitas atau preferensi umum pengguna.

### Solusi 2: Hybrid Recommendations

Solusi kedua adalah Hybrid Recommendations, yang menggabungkan rekomendasi Content-Based Filtering dengan rekomendasi berdasarkan popularitas film. Dalam pendekatan ini, upaya dilakukan untuk memberikan rekomendasi yang lebih seimbang antara preferensi pengguna dan popularitas film.

#### Cara Kerja Hybrid Recommendations:
- Algoritma Hybrid Recommendations menggabungkan hasil dari Content-Based Filtering dan rekomendasi berdasarkan popularitas film.
- Rekomendasi Content-Based Filtering digunakan untuk memberikan film-film dengan atribut konten serupa dengan yang telah disukai pengguna.
- Rekomendasi berdasarkan popularitas film ditambahkan untuk memastikan bahwa film yang populer atau tren saat itu juga mendapatkan perhatian.
- Hasil akhir adalah rekomendasi yang lebih beragam, mencoba memenuhi preferensi individual pengguna sambil mempertimbangkan popularitas film.

#### Kelebihan Hybrid Recommendations:
- Menggabungkan kelebihan Content-Based Filtering dan rekomendasi berdasarkan popularitas untuk memberikan rekomendasi yang lebih beragam.
- Dapat mengatasi beberapa kelemahan dari masing-masing pendekatan.

#### Kekurangan Hybrid Recommendations:
- Memerlukan perhatian khusus dalam menggabungkan hasil dari kedua pendekatan.

  
### Output: Rekomendasi Top-10

Kedua solusi di atas akan menghasilkan rekomendasi top-10 film berdasarkan preferensi pengguna. Rekomendasi ini akan membantu pengguna menemukan film-film yang mungkin mereka nikmati berdasarkan kesamaan konten dan popularitas.

Berikut ini adalah hasil **_Content-Based Recommendation_** dari Spider-Man: No Way Home
|    Index   |       Movie Title       |                 Genres                 |
|:----------:|:-----------------------:|:------------------------------------:|
|    170     |        Spider-Man       |          Fantasy, Action              |
|    4057    | Spider-Man Strikes Back | Action, Adventure, Family, Fantasy, TV Movie |
|    1490    |        Spider-Man       | Science Fiction, Action, Crime, TV Movie |
|    132     |  The Amazing Spider-Man 2 |  Action, Adventure, Fantasy           |
|    7939    | Beyond the Ultimate Spin: The Making of 'Spide... | Documentary |
|    201     |       Spider-Man 3       |   Fantasy, Action, Adventure          |
|     90     | The Amazing Spider-Man  |   Action, Adventure, Fantasy          |
|    168     |  Spider-Man: Homecoming  | Action, Adventure, Science Fiction, Drama |
|    191     | Spider-Man: Into the Spider-Verse | Action, Adventure, Animation, Science Fiction |
|    144     | Spider-Man: Far From Home | Action, Adventure, Science Fiction    |

Berikut ini adalah hasil **_Hybrid Recommendation_** dari The Commando
|   Title            |           Genre                     |
|:------------------:|:---------------------------------:|
|  2 Guns            | Action, Comedy, Crime              |
|  Transit           | Action, Thriller, Crime            |
|  Max Payne         | Crime, Action, Drama, Thriller     |
|  The Night of the Hunter | Crime, Drama, Thriller         |
|  Good People       | Thriller, Crime, Action            |
|  The International | Action, Thriller, Drama, Crime     |
|  Now You See Me    | Thriller, Crime                    |
|  Bad Samaritan     | Thriller, Crime, Horror            |
|  Commando 2 - The Black Money Trail | Action, Thriller      |
|  Ghostland         | Horror, Mystery, Thriller          |

## Evaluation

**Presisi (Precision)**:

Presisi mengukur berapa banyak kasus positif yang diprediksi oleh model yang benar. Ini menghitung rasio True Positives (kasus yang benar-benar termasuk dalam kelas positif) terhadap semua prediksi positif yang dibuat.


$$\text{Presisi} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$

Hasil Presisi untuk  **_Content-Based Recommendation_** dari Spider-Man: No Way Home adalah 100% karena dapat dilihat berdasarkan judul yang sama dan juga genrenya dari hasil diatas bahwa seluruh rekomendasi adalah sekuel Spider-Man.

Hasil Presisi untuk **_Hybrid Recommendation_** dari The Commando adalah (70%) karena dapat dilihat berdasarkan judul yang sama dan juga genrenya dari hasil diatas bahwa genre dari the commando adalah Action, Crime, Thriller sedangkan 2 Guns (Tidak memiliki genre Thriller) Good People (Tidak memiliki genre Thriller) Ghostland (Tidak memiliki genre Action dan Crime)

**Recall (Sensitivitas atau Tingkat Positif Sejati)**:

Recall mengukur seberapa baik model dapat mengidentifikasi semua kasus positif yang sebenarnya. Ini menghitung rasio True Positives (kasus yang benar-benar termasuk dalam kelas positif) terhadap semua kasus positif yang sebenarnya.


$$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$


Hasil Recall untuk  **_Content-Based Recommendation_** dari Spider-Man: No Way Home adalah 100% karena dapat dilihat berdasarkan judul yang sama dan juga genrenya dari hasil diatas bahwa seluruh rekomendasi adalah sekuel Spider-Man.

Hasil Presisi untuk **_Hybrid Recommendation_** dari The Commando adalah (100%) karena dapat dilihat berdasarkan judul yang sama dan juga genrenya dari hasil diatas bahwa genre dari the commando adalah Action, Crime, Thriller sedangkan film yang sesuai dengan preferensi pengguna (Action, Crime, Thriller) tetapi tidak direkomendasikan tidak ada.


**Referensi**
- Roy, D., Dutta, M. A systematic review and research perspective on recommender systems. J Big Data 9, 59 (2022). (https://doi.org/10.1186/s40537-022-00592-5)
- Jayalakshmi S, Ganesh N, Čep R, Senthil Murugan J. Movie Recommender Systems: Concepts, Methods, Challenges, and Future Directions. Sensors (Basel). 2022 Jun 29;22(13):4904. doi: 
  10.3390/s22134904 PMID: 35808398; PMCID: PMC9269752. (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9269752/)

**---Ini adalah bagian akhir laporan---**
