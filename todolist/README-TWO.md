### Rafinal Haryokusumo Taloputra
### 2106634540
### PBP-F

# Tugas 6 PBP

App link to [Heroku](https://fikri-belum-sembuh.herokuapp.com/todolist/login/)

# Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
_Asynchronous programming_ adalah model program dimana lebih dari satu perintah dapat dijalankan pada waktu yang sama. Eksekusi perintah dari _asynchronous programming_ ini tidak memblokir eksekusi perintah lainnya di program yang sama. Contohnya adalah program komunikasi yang digunakan untuk _chat_ dimana pengguna dapat mengirim pesan bersama dengan lawan bicaranya. _Synchronous programming_ adalah model program yang memiliki banyak restriksi sehingga perintah harus dijalankan satu persatu. Jika suatu instruksi dijalankan, program ini akan memblokir instruksi lainnya sampai instruksi yang sedang dijalankan selesai. Model program ini cocok untuk tipe program yang mempunyai sistem reaktif.

# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
_Event-Driven Programming_ adalah paradigma program dimana alur program ditentukan oleh tindakan pengguna seperti mouse click, mengetik, dll. Paradigma ini sering kita jumpai dulu di pelajaran GUI, dimana program akan lanjut berjalan jika kita melakukan tindakan. Contoh penerapannya pada tugas ini adalah untuk login kita perlu click tombol login sehingga dapat melanjutkan program.

# Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan _asynchronous programming_ ada pada tombol create task dimana jika pengguna sudah mengisi judul dan deskripsi serta men-click tombol tersebut, maka program akan langsung memunculkan card yang sudah pengguna isi tadi. Program akan melakukan fungsi addTodolist setelah tombol di click dan setelah berhasil menyimpan data, program akan refresh halaman todolist dengan sendirinya.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat fungsi `show_json` pada `views.py` untuk return data yang dibuat user
2. Membuat routing untuk fungsi tersebut didalam file `urls.py`
3. Membuat fungsi getTodolist dalam `script` menggunakan _fetch_ untuk memanggil fungsi pada `views.py`
4. Membuat form pada `todolist.html` dan menambahkan tombol untuk pengguna agar dapat menambahkan _task_
5. Membuat fungsi `add_task` dalam views.py agar penambahan task berupa _asynchronous programming_
6. Membuat routing untuk fungsi tersebut didalam file `urls.py`
7. Membuat fungsi addTodolist dalam `script` untuk memanggil fungsi pada `views.py`
8. Membuat fungsi `refreshTodolist` untuk refresh halaman utama secara asinkronus  

<img width="960" alt="image" src="https://user-images.githubusercontent.com/89496855/195484805-90796675-10b9-461a-b9c1-bd0643bf0655.png">
