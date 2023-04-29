Kel 6 ASD : Tita Nabila Putri, Nazwa Talisya Inaya, Gunawan
 | Sistem Informasi - B'22

## Deskripsi Program
Pada program Spotify ini memungkinkan pengguna/user untuk membuat playslist dengan menambah lagu, menghapus lagu, melihat display playlist, mencari dan mengurutkan lagu, kemudian beralih ke user premium. Pada penggunaan premium, pengguna/user dapat membeli tiket konser.

## Struktur Project
Aplikasi ini merujuk pada playlist yang memungkinkan kita untuk menambah lagu, menghapus lagu dan melihat display playlist yang programnya saling berkaitan satu sama lain. Ketika kita ingin menambahkan satu atau lebih lagu, maka otomatis lagu tersebut akan masuk pada display playlist. Sementara jika kita ingin menghapus sebuah lagu yang telah ditambahkan pada display playlist, maka lagu tersebut akan terhapus. Lalu kita juga dapat mengurutkan lagu dan ketika ingin mencari lagu di dalam playlist kita dapat mencarinya dengan metode jump search (untuk mencari) dan quick sort (untuk mengurutkan). Login user juga dapat dilakukan untuk user standar dan juga premium.

## Fitur
- MENU AWAL -
1. user registration : pada fitur ini berfungsi untuk registrasi akun pengguna 
2. login user : pada fitur ini berfungsi untuk login pengguna
3. log out : pada fitur ini berfungsi untuk keluar dari menu

- MENU USER STANDAR -
1. Add Song : Menambahkan lagu
2. Remove Song : Menghapus lagu
3. Display Playlist : Isi playlist
4. Search Song : Mencari lagu
5. Sort Playlist : Mengurutkan playlist
6. Beli Premium : Beralih ke mode premium dengan transaksi
7. Saldo : Mengecek saldo yang tersisa
8. Exit : Keluar dari menu 

- MENU USER PREMIUM -
1. Add Song : Menambahkan lagu
2. Remove Song : Menghapus lagu
3. Display Playlist : Isi playlist
4. Search Song : Mencari lagu
5. Display Sorted Playlist : Mengurutkan isi dari playlist
6. Buy Some Concert Tickets : Untuk melakukan pembelian tiket konser
7. Exit : Keluar dari menu 

## Fungsionalitas
Pada program ini, linked list difungsikan agar dapat menyimpan record data yang ada pada masing-masing pilihan. Mulai dari melihat display playlist yang ada, menambah lagu dan menghapus lagu pada playlist. Linked list digunakan dalam pengimplementasian struktur data yang terdiri dari urutan record data dimana setiap record memiliki field yang menyimpan alamat record data selanjutnya di dalam urutan. Artinya, setiap elemen memiliki keterkaitan dengan elemen berikutnya yang membuat pemrograman menjadi lebih efisien dan terstruktur sehingga dapat secara otomatis membuat suatu tempat baru untuk menyimpan data. Kemudian algoritma searching difungsikan untuk mencari lagu yang ada di dalam playlist, sementara sorting untuk mengurutkan lagu di dalam playlist. Terdapat juga Login multiuser untuk user standar/biasa dan user premium. Pada user premium terdapat priviledge untuk membeli tiket konser dengan harga yang terjangkau.

## Cara Penggunaan
Saat di-run, program akan menampilkan pilihan kepada user untuk melakukan registrasi terlebih dahulu, kemudian login, lalu akan ditampilkan menu ingin melakukan apa. Jika user memilih/menginputkan pilihan pertama yaitu Add Song, maka user akan diminta memasukkan judul, penyanyi dan durasi lagu yang nantinya akan otomatis masuk pada Display Playlist di pilihan pertama dan pada saat kita membuka Display Playlist kembali, maka akan tertera judul, penyanyi dan durasi yang telah dimasukkan. Selanjutnya ketika user menginput pilihan kedua yaitu Remove Lagu, maka user hanya akan diminta untuk memasukkan judul lagu yang ingin dihapus. Dan apabila lagu telah terhapus, maka lagu tersebut otomatis juga hilang/terhapus dari Display Playlist. Kemudian pada pilihan ketiga yaitu Display Playlist, maka akan ditampilkan lagu-lagu apa saja yang ada di dalam playlist. Jika belum ada lagu yang ditambahkan, maka program akan menampilkan/memberitahukan bahwa isi playlist masih kosong. Lalu ketika user menginput pilihan keempat yaitu mencari lagu yang ada dalam playlist, jadi user memasukkan judul lagu yang ingin dicari. Pilihan kelima yaitu mengsorting data yang tidak berurut menjadi data yang terurut. Keenam adalah pilihan jika user standar ingin beralih ke premium, dan jika sudah beralih ke premium maka saldo akan berkurang. Lalu jika user memilih pilihan ke tujuh adalah sisa saldo yang tersedia. Kemudian pada pilihan ke delapan yaitu Exit, maka program akan terhenti. Sementara jika user menginputkan pilihan angka yang tidak tertera pada pilihan, maka akan diberitahukan bahwa pilihan tidak tersedia. Untuk menu pada user premium yang keenam adalah pilihan tiket konser, jadi pada user premium dapat melakukan pembelian tiket konser dengan harga terjangkau yang sudah tersedia dan tinggal memasukkan nama dan tiket konser yang ingin dibeli.
