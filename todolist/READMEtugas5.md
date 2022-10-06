### Rafinal Haryokusumo Taloputra
### 2106634540
### PBP-F

# Tugas 5 PBP

App link to [Heroku](https://fikri-belum-sembuh.herokuapp.com/todolist/login/)

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS : Digunakan untuk men-_style_ suatu elemen pada HTML. Penggunaan inline CSS harus menuliskan _style_ pada setiap elemen dalam HTML. Manfaat dari method ini yaitu memudahkan kita untuk meng-_edit_ css karena sudah satu file pada HTML dan kita juga tidak perlu membuat _file_ baru yang berisikan CSS. Kelemahan Inline CSS adalah penulisan _style_ pada setiap elemen HTML akan menghabiskan waktu dan mengacaukan struktur _file_ HTML.

Internal CSS : Efektif digunakan untuk men-_style_ suatu page. Penggunaan internal css memerlukan kita untuk menambah tag _style_ didalam elemen _head_ pada suatu file HTML. Manfaat dari method ini adalah kita tidak perlu meng-_upload_ file-file lain untuk website kita. Kelemahannya adalah penambahan _style_ dapat membuat ukuran _page_ menjadi lebih besar dan memerlukan waktu yang lebih untuk aksesnya.

External CSS : Efektif digunakan untuk pembuatan _website_ dalam ukuran besar (ada banyak page). Penggunaan external css memerlukan kita untuk menuliskan kode css pada file yang berbeda dengan HTML. Kelebihan dari metode ini adalah struktur HTML yang lebih rapi karena tidak dibuat bersama dengan css dan satu file css dapat digunakan untuk banyak _page_. Kelemahannya adalah _page_ tidak dapat di _render_ sepenuhnya jika file css belum ter-_upload_.

## Jelaskan tag HTML5 yang kamu ketahui.
Tag :
1. <!DOCTYPE> , untuk menentukan tipe dokumen
2. <html> , untuk membuat dokumen HTML
3. <title>, untuk judul suatu page
4. <p> , untuk menuliskan paragraf pada page
5. <h1>...<h6> , untuk heading suatu page
6. <br> , untuk membuat baris kosong
7. <!--...--> , untuk menuliskan komen
8. <form> , untuk membuat form input bagi user
9. <input> , untuk input user
10. <button> , untuk tombol yang dapat di klik user

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Simple Selectors , memilih elemen untuk di _style_ berdasarkan nama, id, atau class
2. Attribute Selectors , memilih elemen untuk di _style_ berdasarkan atribut atau nilainya
3. Element Selectors, memilih elemen untuk di _style_ berdasarkan nama elemen tersebut

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menambahkan bootstrap ke base.html
2. Menggunakan External CSS dengan membuat folder `static` yang berisi file CSS yang akan digunakan
3. Men-_design_ page menggunakan CSS dan Bootstrap
4. Menggunakan _media query_ untuk membuat page menjadi responsive