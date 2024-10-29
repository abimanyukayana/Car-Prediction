# Car Price Prediction
## Project Overview 📚

Project ini memiliki tujuan sebagai berikut:

- Memahami konsep Machine Learning secara keseluruhan 🤖.
- Mempersiapkan data untuk digunakan dalam model Supervised Learning (Classification atau Regression) 📊.
- Mengimplementasikan Supervised Learning (Classification atau Regression) dengan data yang dipilih 🔍.
- Melakukan Hyperparameter Tuning dan Model Improvement 🔧.
- Melakukan Model Deployment 🚀.

## Dataset 📦

Dataset yang digunakan dalam proyek ini diambil dari [Kaggle]([https://www.kaggle.com/](https://www.kaggle.com/datasets/lainguyn123/australia-car-market-data). Dataset ini memiliki minimal 10 kolom dengan campuran kolom kategorikal dan numerikal. Semua kolom memiliki deskripsi yang jelas, dan data telah diperiksa untuk memastikan kesesuaian dengan kriteria yang ditetapkan.

## Problem Statement 📝

Dalam industri otomotif, harga mobil merupakan faktor penting yang mempengaruhi keputusan pembelian konsumen. Namun, dengan banyaknya variabel yang mempengaruhi harga mobil, seperti merek, model, tahun produksi, kondisi, dan fitur tambahan, seringkali sulit bagi pembeli untuk menentukan apakah harga yang ditawarkan adalah adil. Oleh karena itu, proyek ini bertujuan untuk mengembangkan model prediksi harga mobil menggunakan teknik Machine Learning, dengan mempertimbangkan berbagai fitur mobil yang relevan.

Model ini akan menganalisis data historis penjualan mobil untuk memberikan perkiraan harga yang lebih akurat berdasarkan karakteristik mobil yang berbeda. Dengan demikian, konsumen dapat membuat keputusan yang lebih baik dan penjual dapat menetapkan harga yang kompetitif.

Alasan Mengapa Masalah Ini Penting:

Membantu Konsumen: Memberikan informasi harga yang akurat membantu konsumen dalam membuat keputusan pembelian yang tepat dan menghindari penipuan.
Optimalisasi Penjualan: Penjual dapat menentukan harga yang sesuai berdasarkan analisis pasar, meningkatkan peluang penjualan.
Analisis Tren Pasar: Dengan memprediksi harga, analisis dapat dilakukan untuk memahami tren pasar otomotif dan faktor-faktor yang mempengaruhi perubahan harga.
Efisiensi Waktu: Mempermudah proses pencarian harga mobil bagi pembeli dengan memberikan estimasi harga secara otomatis, sehingga menghemat waktu dan usaha.


## Outline Proyek 📋

Proyek ini terdiri dari beberapa langkah berikut:

1. **Perkenalan**: Identitas dan gambaran besar dataset yang digunakan.
2. **Import Libraries**: Memuat semua library yang diperlukan 📦.
3. **Data Loading**: Proses penyiapan data sebelum eksplorasi lebih lanjut.
4. **Exploratory Data Analysis (EDA)**: Melakukan analisis eksplorasi pada dataset 🔍.
5. **Feature Engineering**: Menyiapkan data untuk pelatihan model ⚙️.
6. **Model Definition**: Mendefinisikan model yang akan digunakan.
7. **Model Training**: Melatih model dengan berbagai hyperparameter 💪.
8. **Model Evaluation**: Mengevaluasi performa model 📈.
9. **Model Saving**: Menyimpan model terbaik untuk digunakan di masa depan 💾.
10. **Model Inference**: Menguji model dengan data baru 🧪.
11. **Pengambilan Kesimpulan**: Menyimpulkan hasil dari analisis yang dilakukan 🔍.

## Requirements 📋

Proyek ini menggunakan beberapa library, di antaranya:

- Scikit-Learn
- Matplotlib
- Seaborn

## Model Deployment 🚀

Folder `deployment` berisi file-file yang diperlukan untuk model deployment. Pastikan untuk mengacu pada file `url.txt` untuk informasi lebih lanjut mengenai dataset dan deployment.

## Conclusion 🎉

Proyek prediksi harga mobil ini bertujuan untuk memberikan solusi bagi konsumen dan penjual dalam menentukan harga yang adil dan kompetitif di pasar otomotif. Dengan memanfaatkan teknik Machine Learning, proyek ini tidak hanya membantu konsumen dalam membuat keputusan pembelian yang lebih tepat tetapi juga memungkinkan penjual untuk mengoptimalkan strategi harga berdasarkan analisis pasar yang mendalam. Melalui langkah-langkah sistematis mulai dari pemuatan data hingga evaluasi model, proyek ini mengedepankan pentingnya data yang berkualitas dan analisis yang cermat untuk menghasilkan model prediksi yang efektif.

Dengan model yang berhasil di-deploy, pengguna dapat dengan mudah mengakses estimasi harga berdasarkan fitur-fitur mobil yang relevan, sehingga meningkatkan efisiensi dalam proses pencarian harga. Di akhir proyek, diharapkan dapat memberikan wawasan yang lebih baik mengenai tren pasar otomotif dan membantu semua pihak yang terlibat untuk mengambil keputusan yang lebih informasional dan berorientasi pada data.
