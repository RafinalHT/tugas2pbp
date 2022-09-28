### Rafinal Haryokusumo Taloputra
### 2106634540
### PBP-F

# Tugas 4 PBP

App link to [Heroku](https://fikri-belum-sembuh.herokuapp.com/todolist/login/)

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
CSRF token pada elemen `<form>` berguna untuk melindungi _website_ dari serangan CSRF (_Cross-Site Request Forgery_). CSRF token adalah token unik yang selalu berubah setiap sesi _user_ dan nilainya biasanya sangat besar sehingga lebih susah ditebak oleh peretas. Jika kode ini tidak ada dalam elemen `<form>`, maka server akan menolak request client dan memunculkan error karena _Invalid or missing CSRF token_ 
