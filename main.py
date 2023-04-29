# bagian tita dan nazwa
import csv
import os
os.system('cls')
import mysql.connector

from database import db
from song import Song
from playlist import Playlist
from playlist_manager import PlaylistManager
from playlist import User
from ticket import show_tickets
from invoice import print_invoice




def tampilan(username):
    playlist_manager = PlaylistManager()
    try:
        while True:
            print("|==================================|")    
            print("|----------------------------------|")
            print("|>>>>>>> 【ｓｐｏｔｉｆｙ】<<<<<<<  |")
            print("|----------------------------------|")
            print("|==================================|")
            print("| 1. Add Song                      |")
            print("| 2. Remove Song                   |")
            print("| 3. Display Playlist              |")
            print("| 4. Search Song                   |")
            print("| 5. Sort Playlist                 |")
            print("| 6. Play Song                     |")
            print("| 7. Beli premium                  |")
            print("| 8. Exit                          |")
            print("|==================================|")

            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                title = input("Enter song title: ")
                artist = input("Enter artist name: ")
                playlist_manager.add_song(username, title, artist)
            elif choice == '2':
                title = input("Enter song title: ")
                playlist_manager.delete_song_from_file(username, title)
            elif choice == '3':
                playlist_manager.display(username)
            elif choice == '4':
                titles = input("Enter song title: ")
                playlist_manager.search_song_file(username, titles)
            elif choice == '5':
                playlist_manager.display_sorted(username, from_file= True)
            elif choice == '6':
                song_title = input("Enter the title of the song you want to play: ")
                playlist_manager.play_song(song_title)
            elif choice == '7':
                print("Anda akan membeli premium.")
                jawaban = input("Apakah anda yakin? (y/n) ")
                if jawaban == "y":
                    # Beli premium dan ubah jenis_user menjadi "premium"
                    beli_premium(username)
                    print("Terima kasih telah membeli premium.")
                    tampilan_premium()
                else:
                    print("Batal membeli premium.")
            elif choice == '8':
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please choose again.")
    except KeyboardInterrupt:
        print("Invalid choice!")
        back = input("Want to repeat?  ")
        if back == "y":
            tampilan()
        elif back == "n":
            exit()

# akun premium
def tampilan_premium():
    playlist_manager = PlaylistManager()
    while True:
        print("|==================================|")
        print("|----------------------------------|")
        print("|>>>>>>> 【ｓｐｏｔｉｆｙ】 <<<<<<<|")
        print("|----------------------------------|")
        print("|==================================|")
        print("| 1. Add Song                      |")
        print("| 2. Remove Song                   |")
        print("| 3. Display Playlist              |")
        print("| 4. Search Song                   |")
        print("| 5. Display Sorted Playlist       |")
        print("| 6. Buy Some Concert Tickets      |")
        print("| 7. Exit                          |")
        print("|==================================|")
        try:
            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                title = input("Enter song title: ")
                artist = input("Enter artist name: ")
                song = Song(title, artist)
                playlist_manager.add_song_premium(song)
            elif choice == '2':
                title = input("Enter song title to remove: ")
                playlist_manager.remove_song_premium(title)
            elif choice == '3':
                playlist_manager.display_playlist_premium()
            elif choice == '4':
                judul = input("Enter song title to search : ")
                playlist_manager.search_song_premium(judul)
            elif choice == '5':
                playlist_manager.display_sorted_music_by_song_name_premium()
            elif choice == '6':
                show_tickets()
                customer_name = input("Enter customer name: ")
                ticket_id = int(input("Enter ticket ID: "))
                qty = int(input("Enter the number of tickets: "))
                file_path = 'invoice.csv' # tambahkan parameter file_path
                print_invoice(customer_name, ticket_id, qty, file_path) # sertakan parameter file_path7
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please choose again.")
        except Exception as e:
            print(f"Error: {e}")
            print("Please try again from the beginning.")

def beli_premium(username):
    # Membuat cursor
    mycursor = db.cursor()

    # Mengeksekusi query untuk mengubah jenis_user menjadi "premium"
    sql = "UPDATE users SET jenis_user = 'premium' WHERE username = %s"
    val = (username,)
    try:
        mycursor.execute(sql, val)
        # Menyimpan perubahan
        db.commit()
        print(mycursor.rowcount, "record updated.")
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

def login():
    playlist_manager = PlaylistManager()
    while True:
        print("1. User Registration")
        print("2. Login User")
        print("3. Log Out")
        input_login = input("Please select login :")
        
        if input_login == "1":
            nama = input("Your Name : ")
            regis1 = input("Enter username : ")
            regis2 = input("Enter password : ")
            
            # membuat cursor
            mycursor = db.cursor()

            # mengeksekusi query untuk menambahkan akun ke tabel
            sql = "INSERT INTO users (nama, username, password, jenis_user) VALUES (%s, %s, %s, %s)"
            val = (nama, regis1, regis2, "standar")
            try:
                mycursor.execute(sql, val)
                # menyimpan perubahan
                db.commit()
                print(mycursor.rowcount, "account created.")
                playlist_manager.register_user(regis1, regis2)
                User(regis1, regis2)
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
            print()
            
        elif input_login == "2":
            loginuser = input('Enter username: ')
            loginpass = input('Enter Password: ')
            
            # Membuat cursor
            mycursor = db.cursor()
            
            # Mengeksekusi query untuk memilih akun berdasarkan username dan password
            sql = "SELECT jenis_user FROM users WHERE username = %s AND password = %s"
            val = (loginuser, loginpass)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()
            
            if result:
                jenis_user = result[0]
                print(f"Welcome {loginuser}, your account type is {jenis_user}")
                if jenis_user == "standar":
                    # Memanggil fungsi tampilan untuk standard user
                    tampilan(loginuser)
                elif jenis_user == "premium":
                    # Memanggil fungsi tampilan_premium untuk premium user
                    tampilan_premium()
            else:
                print("Username atau Password Salah")
                
        elif input_login == "3":
            break

login()
# selesai tita dan nazwa
