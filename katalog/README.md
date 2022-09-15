# Tugas 2 PBP

App link to [Heroku](https://fikri-belum-sembuh.herokuapp.com/katalog/)

## Bagan yang berisi request client ke web aplikasi berbasis Django

## Kenapa menggunakan _virtual environment_? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?
_Virtual environment_ adalah alat yang dapat kita gunakan untuk menjaga _dependencies_ yang diperlukan dan menyimpan _project_ agar tetap terisolasi. Tanpa _virtual environment_, semua _project_ django yang kita kerjakan bisa berbentrokan satu sama lain karena perbedaannya _requirements_. Kita tetap dapat membuat aplikasi web berbasis Django tanpa _virtual environment_, tetapi jika kita ingin membuat _project_ Django lainnya bisa terjadi bentrok karena perbedaan _requirements_.   

## Cara implementasi poin 1-4
### Poin 1
Membuat fungsi `show_katalog` dengan parameter _request_ didalam `views.py` pada folder katalog. Fungsi tersebut membuat variabel `data_katalog` yang berisikan semua objek dari `CatalogItem` yang berada pada `models.py` dalam folder katalog. Fungsi juga membuat _context_ yang berisikan `list_katalog`, nama, dan npm. Terakhir, fungsi akan _return_ render `katalog.html` yang berisikan data dari context.
### Poin 2
Menambahkan `path('', show_katalog, name='show_katalog'),` dalam file `urls.py` pada folder katalog dan memindahkan rutenya ke _website_ dengan menambahkan url tersebut kedalam daftar url _project_ didalam folder `project_django`.
### Poin 3
Pada file `katalog.html`, tambahkan looping untuk mengambil data-data yang ada di `list_katalog` dan _print_ data-data tersebut sesuai urutan tabel
### Poin 4
Buatlah app pada Heroku dan tambahkan dua secrets didalam repository yaitu `HEROKU_APP_NAME` dan `HEROKU_API_KEY` untuk menghubungkan github ke heroku. Jika sudah ditambahkan, _project_ dapat dilihat di aplikasi heroku seperti ini:

![image](https://user-images.githubusercontent.com/89496855/190291295-07a2e69c-c408-4cde-8fdf-f75702de8d82.png)
