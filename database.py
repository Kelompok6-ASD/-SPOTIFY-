import mysql.connector

# Membuat koneksi ke database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="music_player"
)