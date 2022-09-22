### Rafinal Haryokusumo Taloputra
### 2106634540
### PBP-F

# Tugas 3 PBP

App link to [Heroku](https://fikri-belum-sembuh.herokuapp.com/mywatchlist/)

## Perbedaan JSON, XML, dan HTML 
JSON adalah format pertukaran data yang ringan dan bisa digunakan untuk semua bahasa pemrograman. JSON merupakan cara untuk merepresentasikan suatu objek dalam bentuk key dan value.

XML adalah suatu _markup language_ yang bertujuan untuk membawa data dan menuliskan kode dalam format yang mampu dibaca manusia dan mesin. XML relatif lebih aman daripada JSON dan data-data didalamnya lebih sulit dibandingkan JSON untuk dibaca.

HTML adalah _markup language_ standar yang digunakan untuk membangun suatu _website_. Berbeda dengan XML dan JSON, HTML berfungsi untuk menggambarkan struktur dari website dan menampilkan data-data yang ada ke suatu website 

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Pembangunan suatu platform pasti membutuhkan pertukaran data seperti pertukaran data user dan data platform maupun pertukaran data sesama user. _Data delivery_ disini dapat digunakan untuk mempermudah dan mempercepat pertukaran data sehingga para _programmer_ tidak perlu mengkhawatirkan pertukaran data secara manual lagi.

## Bagaimana cara kamu mengimplementasikan checklist Tugas 3
1. Buat aplikasi baru bernama _mywatchlist_ dengan `python manage.py startapp mywatchlist`
2. Pada folder `project_django`, tambahkan path _mywatchlist_ kedalam urls.py dan tambahkan juga _mywatchlist_ sebagai salah satu Installed_Apps didalam settings.py
3. Pada folder utama, ubah baris pertama dari file _Procfile_ menjadi `release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_mywatchlist_data.json'`
4. Dalam folder _mywatchlist_, tambahkan folder fixtures yang akan berisi `initial_mywatchlist_data.json` untuk penyajian data yang akan digunakan untuk aplikasi
5. Tambahkan fungsi untuk menyajikan data pada `views.py` dalam _mywatchlist_ dan tambahkan path-path untuk HTML, XML, dan JSON pada `urls.py`
6. Buat model pada `models.py` untuk variable-variable yang akan disajikan
7. Migrate perubahan yang dilakukan dan lakukan perintah `python manage.py loaddata initial_wishlist_data.json`


# URLS Postman

HTML
![html](https://user-images.githubusercontent.com/89496855/191543190-8c98cea4-5205-4b6f-80f0-853151990d34.png)

JSON
![json](https://user-images.githubusercontent.com/89496855/191543263-8c8b8638-c1e6-4336-9350-4f99014b0800.png)

XML
![xml](https://user-images.githubusercontent.com/89496855/191543313-c914c215-11df-4bbf-a325-e2a0d5a95c5b.png)
