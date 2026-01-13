# Prediksi Harga Rumah Bandung

Aplikasi Prediksi Harga Rumah Kota Bandung Menggunakan Machine Learning dan FastAPI

---

## 1. Pendahuluan

Perkembangan teknologi data dan Machine Learning memungkinkan pemanfaatan data historis untuk membantu pengambilan keputusan di berbagai bidang, termasuk sektor properti. Harga rumah merupakan salah satu faktor penting yang dipengaruhi oleh banyak variabel seperti luas tanah, luas bangunan, jumlah kamar tidur, dan jumlah kamar mandi.

Proyek **Prediksi Harga Rumah Bandung** ini bertujuan untuk membangun sebuah sistem prediksi harga rumah di Kota Bandung berbasis **Machine Learning** yang dapat diakses melalui **API dan antarmuka web**. Sistem ini diharapkan dapat membantu pengguna dalam memperkirakan harga rumah berdasarkan karakteristik fisik properti.

---

## 2. Tujuan Proyek

Tujuan dari pengembangan proyek ini adalah:

1. Mengolah dataset harga rumah Kota Bandung menjadi data yang siap digunakan untuk pemodelan.
2. Membangun model Machine Learning untuk memprediksi harga rumah.
3. Mengimplementasikan model ke dalam REST API menggunakan FastAPI.
4. Menyediakan antarmuka web sederhana untuk melakukan prediksi secara interaktif.
5. Mendokumentasikan keseluruhan proses pengembangan sistem secara teknis.

---

## 3. Ruang Lingkup Sistem

Ruang lingkup sistem dalam proyek ini meliputi:

* Prediksi harga rumah hanya untuk wilayah **Kota Bandung**
* Variabel input:

  * Luas tanah (m²)
  * Luas bangunan (m²)
  * Jumlah kamar tidur
  * Jumlah kamar mandi
* Output:

  * Harga rumah dalam satuan **miliar rupiah**
* Sistem tidak mempertimbangkan faktor eksternal seperti lokasi spesifik, kondisi lingkungan, atau fasilitas umum.

---

## 4. Dataset

Dataset yang digunakan merupakan data harga rumah di Kota Bandung yang dikumpulkan dari sumber publik.

### 4.1 Atribut Dataset

Atribut yang digunakan dalam pemodelan:

| Atribut       | Deskripsi                         |
| ------------- | --------------------------------- |
| luas_tanah    | Luas tanah dalam meter persegi    |
| luas_bangunan | Luas bangunan dalam meter persegi |
| kamar_tidur   | Jumlah kamar tidur                |
| kamar_mandi   | Jumlah kamar mandi                |
| harga         | Harga rumah (miliar rupiah)       |

### 4.2 Pembersihan Data

Tahapan pembersihan data meliputi:

* Ekstraksi nilai numerik dari data teks
* Konversi tipe data ke numerik
* Penghapusan data kosong (missing values)
* Penyaringan data tidak wajar (outlier)

---

## 5. Metodologi Machine Learning

### 5.1 Algoritma

Model yang digunakan adalah **Linear Regression**, karena sederhana, mudah diinterpretasikan, dan sesuai untuk permasalahan regresi numerik.

### 5.2 Pipeline Model

Model dibangun menggunakan pipeline dengan tahapan:

1. StandardScaler
2. Linear Regression

Model yang telah dilatih disimpan dalam file:

```
bandung_house_price_model.pkl
```

---

## 6. Arsitektur Sistem

Sistem terdiri dari tiga komponen utama:

1. **Frontend (Web Interface)**

   * HTML dan Tailwind CSS
   * Input data dan tampilan hasil prediksi

2. **Backend (FastAPI)**

   * Menyediakan REST API
   * Mengelola request dan response

3. **Model Machine Learning**

   * Model Linear Regression

Alur sistem:

```
User → Web → FastAPI → Model → FastAPI → Web
```

---

## 7. Implementasi API

### Endpoint Prediksi

**POST /predict**

Contoh request:

```json
{
  "luas_tanah": 120,
  "luas_bangunan": 90,
  "kamar_tidur": 3,
  "kamar_mandi": 2
}
```

Contoh response:

```json
{
  "predicted_price_miliar": 1.75,
  "note": "Harga berdasarkan pola data rumah di Kota Bandung"
}
```

---

## 8. Antarmuka Pengguna

Antarmuka pengguna berupa halaman web yang memungkinkan pengguna:

* Menginput data rumah
* Mengirim data ke API
* Melihat hasil prediksi secara langsung

---

## 9. Struktur Folder Proyek

```
prediksi-harga-rumah-bandung/
│
├── dataset/
│   └── harga_rumah_bandung.csv
├── train_model.py
├── main.py
├── bandung_house_price_model.pkl
├── index.html
├── README.md
└── requirements.txt
```

---

## 10. Cara Menjalankan Proyek

### 10.1 Clone Repository

```bash
git clone https://github.com/USERNAME/prediksi-harga-rumah-bandung.git
cd prediksi-harga-rumah-bandung
```

### 10.2 Install Dependency

```bash
pip install -r requirements.txt
```

### 10.3 Training Model (Opsional)

```bash
python train_model.py
```

### 10.4 Menjalankan API

```bash
uvicorn main:app --reload
```

API berjalan di:

```
http://127.0.0.1:8000
```

---

## 11. Kesimpulan

Proyek ini berhasil membangun sistem prediksi harga rumah berbasis Machine Learning dengan arsitektur sederhana dan fungsional. Sistem dapat dikembangkan lebih lanjut dengan penambahan fitur lokasi, evaluasi model, serta deployment ke cloud.

---

## 12. Penutup

Dokumentasi ini dibuat sebagai laporan teknis untuk menjelaskan keseluruhan proses pengembangan proyek Prediksi Harga Rumah Bandung.
