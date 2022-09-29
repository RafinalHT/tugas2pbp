### Rafinal Haryokusumo Taloputra
### 2106634540
### PBP-F

# Tugas 4 PBP

App link to [Heroku](https://fikri-belum-sembuh.herokuapp.com/todolist/login/)

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
CSRF token pada elemen `<form>` berguna untuk melindungi _website_ dari serangan CSRF (_Cross-Site Request Forgery_). CSRF token adalah token unik yang selalu berubah setiap sesi _user_ dan nilainya biasanya sangat besar sehingga lebih susah ditebak oleh peretas. Jika kode ini tidak ada dalam elemen `<form>`, maka server akan menolak request client dan memunculkan error karena _Invalid or missing CSRF token_.
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, caranya adalah dengan menambahkan elemen `<form>` yang berisikan _input_ yang kita masukkan.
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pengguna mengisi submisi form lalu menekan tombol submit untuk mengirimkan HTTP Request ke server. Setelah menekan tombol submit, server akan mencari fungsi `views.py` yang berkaitan dan jika input sudah sesuai, fungsi akan membuat objek dari model input-input yang diterima dan menyimpannya ke _database_. Penampilan data ke template HTML diambil dari data-data yang ada di database dengan menggunakan fungsi `show_todolist` dimana fungsi tersebut menampilkan context yang telah dibuat yaitu data yang telah dimasukkan pengguna.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
  1. Membuat aplikasi todolist dengan kode `python manage.py startapp todolist` pada directory repo tugas
  2. Membuat path ke aplikasi todolist dalam folder `project_django` di `urls.py` dan menambahkan todolist ke dalam INSTALLED_APPS yang ada di file `settings.py`
  3. Dalam folder todolist, buatlah model Task di file `models.py` dengan atribut yang sesuai pada soal
  4. Mengimplementasikan form registrasi, login, dan logout dari tutorial 3
  5. Membuat file html `todolist.html` dan menambahkan fungsi pada `views.py` yang berfungsi untuk menampilkan data yang telah dimasukkan pengguna, tombol logout, dan opsi untuk membuat task baru
  6. 
  
