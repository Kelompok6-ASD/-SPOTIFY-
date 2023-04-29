from playlist import Playlist
from playlist import User
from song import Song
from linked_list import LinkedList
from database import db


class PlaylistManager:
    def __init__(self):
        self.head = None
        self.playlist = Playlist()
        self.linked_list = LinkedList()
        self.users = []

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        print(f"{username} has been registered.")
        user.save_playlist()  # tambahan pemanggilan method save_playlist

    def add_song(self, username, title, artist):
        user = User(username, '')
        if user:
            if self.linked_list.tail and len(self.linked_list) == 5:
                print("Playlist is full! You cannot add more songs.")
                return
            song = Song(title, artist)
            self.linked_list.add_node(song)
            user = User(username, '')
            user.playlist = self
            user.save_playlist()
            print(f"{title} by {artist} has been added to {username}'s playlist.")
            # print(self.linked_list)
            
        else:
            print(f"{username} is not registered.")

    def add_song_premium(self, song):
        # membuat cursor
        mycursor = db.cursor()

        # cek apakah lagu sudah ada di database
        query = "SELECT * FROM musics_premium WHERE title = %s AND artist = %s"
        val = (song.title, song.artist)
        mycursor.execute(query, val)
        result = mycursor.fetchall()
        if len(result) > 0:
            print(f"{song.title} already exists in the playlist.")
        else:
            # tambahkan lagu ke database
            mycursor.execute("INSERT INTO musics_premium (TITLE, ARTIST) VALUES (%s, %s)", (song.title, song.artist))
            db.commit()
            print(f"{song.title} has been added to the playlist!")

    
    def remove_song_premium(self, title):
        # membuat cursor
        mycursor = db.cursor()
        # hapus lagu dari database
        mycursor.execute("DELETE FROM musics_premium WHERE TITLE=%s", (title,))
        db.commit()
        print(f"{title} has been removed from the playlist.")

    
    def display_playlist_premium(self):
        # membuat cursor
        mycursor = db.cursor()
        # ambil semua lagu dari database dan tampilkan
        mycursor.execute("SELECT TITLE, ARTIST FROM musics_premium;")
        cursor = mycursor.fetchall()
        if cursor is not None:
            print("{:<30} {:<30}".format("Title", "Artist"))
            for row in cursor:
                print("{:<30} {:<30}".format(row[0], row[1]))

        
    def search_song_premium(self, title):
        # membuat cursor
        mycursor = db.cursor()

        # query untuk mencari lagu berdasarkan judul
        query = "SELECT * FROM musics_premium WHERE title=%s"
        val = (title,)

        # eksekusi query
        mycursor.execute(query, val)

        # ambil hasil pencarian
        result = mycursor.fetchall()

        # cek apakah lagu ditemukan atau tidak
        if len(result) > 0:
            print("Lagu ditemukan:")
            print("Title\tArtist")
            for song in result:
                print("{}\t{}".format(song[1], song[2]))
        else:
            print("Lagu tidak ditemukan.")


    def display_sorted_music_by_song_name_premium(self):
        # membuat cursor
        mycursor = db.cursor()

        # query data dari tabel musics yang sudah terurut berdasarkan kolom "title"
        mycursor.execute("SELECT * FROM musics_premium ORDER BY title ASC")
        result = mycursor.fetchall()

        # tampilkan data hasil sorting
        print("{:<30} {:<30}".format("Title", "Artist"))
        for row in result:
            print("{:<30} {:<30}".format(row[1], row[2]))


    def remove_song(self, username, title):
        user = User(username, '')
        if user:
            if user.playlist.linked_list.remove_node(Song(title, "")):
                print(f"{title} has been removed from {username}'s playlist.")
            else:
                print(f"{title} is not in {username}'s playlist.")
        else:
            print(f"{username} is not registered.")

    def delete_song_from_file(self, username, title):
        user = User(username, '')
        if user:
            # membuka file playlist
            with open(f"{username}_playlist.txt", "r") as f:
                # membaca file baris per baris
                lines = f.readlines()

            # mencari baris yang mengandung judul lagu
            filtered_lines = [line for line in lines if title not in line]

            # menulis ulang file tanpa baris yang mengandung judul lagu
            with open(f"{username}_playlist.txt", "w") as f:
                f.writelines(filtered_lines)
                print(f"{title} has been removed from {username}'s playlist.")
                user.save_playlist()
        else:
            print(f"{username} is not registered.")

    def display(self, username):
        user = User(username, '')
        if user:
            try:
                with open(f"{username}_playlist.txt", "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print(f"{username}'s playlist is empty.")
        else:
            print(f"{username} is not registered.")


    def play_song(self, username, title):
        user = self._get_user(username)
        if user:
            found = False
            for song in user.playlist.linked_list:
                if song.title.lower() == title.lower():
                    found = True
                    print(f"Now playing {song.title}-{song.artist}")
                    break
            if not found:
                print(f"{title} is not in {username}'s playlist.")
        else:
            print(f"{username} is not registered.")



    def display_sorted(self, username, from_file=False):
        user = User(username, '')
        if from_file:
            # membuka file playlist
            with open(f"{username}_playlist.txt", "r") as f:
                # membaca file baris per baris
                lines = f.readlines()
            # membuat daftar putar dari file
            file_playlist = Playlist()
            for line in lines:
                # memecah setiap baris berdasarkan tanda '-' 
                # dan menyimpan hasilnya ke variabel 'title' dan 'artist'
                title, artist = line.strip().split("-")
                # menambahkan lagu ke playlist
                file_playlist.add_song(username, title.strip(), artist.strip())
            # mengurutkan daftar putar dari file
            sorted_playlist = PlaylistManager.quick_sort(file_playlist.get_song_list())
        else:
            # mengambil daftar putar dari objek User
            if user:
                sorted_playlist = PlaylistManager.quick_sort(user.playlist.get_song_list())
            else:
                sorted_playlist = PlaylistManager.quick_sort(self.playlist.get_song_list())

        sorted_title_list = [song.title for song in sorted_playlist]
        if not sorted_title_list:
            print(f"{username}'s playlist is empty.")
        else:
            if from_file:
                print(f"Sorted playlist from file for {username}:")
            else:
                print(f"Sorted playlist for {username}:")
            for i, title in enumerate(sorted_title_list):
                print(f"{i+1}. {title}")
        if not user:
            print(f"{username} is not registered.")

    def _get_user(self, username):
        for user in self.users:
            if user.username == username or user.username == User(username):
                return user
        return None


    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = []
            greater = []
            for i in range(1, len(arr)):
                if arr[i].title < pivot.title:
                    less.append(arr[i])
                else:
                    greater.append(arr[i])
            return PlaylistManager.quick_sort(less) + [pivot] + PlaylistManager.quick_sort(greater)

    def jump_search(arr, x):
        n = len(arr)
        step = int(n ** 0.5)
        prev = 0
        while arr[min(step, n)-1] < x:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1
        while arr[prev] < x:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev] == x:
            return prev
        return -1

    def search_song_file(self, username, title):
        user = User(username, '')
        if user:
            try:
                with open(f"{username}_playlist.txt", "r") as f:
                    lines = f.readlines()
                    songs = []
                    for line in lines:
                        song_title, artist = line.strip().split("-")
                        songs.append(song_title.strip())
                    index = PlaylistManager.jump_search(songs, title)
                    if index < len(songs):
                        print(f"Song '{title}' found in {username}'s playlist at index {index}.")
                    else:
                        print(f"Song '{title}' not found in {username}'s playlist.")
                    return index
            except FileNotFoundError:
                print(f"{username}'s playlist is not found.")
        else:
            print(f"{username} is not registered.")


    def search_song(self, username, title):
        user = self._get_user(username)
        if user:
            index = PlaylistManager.jump_search(user.playlist.linked_list, title)
            if index == -1:
                print(f"{title} is not found in {username}'s playlist.")
            else:
                print(f"{title} is found at index {index} in {username}'s playlist.")
        else:
            print(f"{username} is not registered in the system.")