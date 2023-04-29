from linked_list import LinkedList
from song import Song


class Playlist:
    def __init__(self):
        self.linked_list = LinkedList()

    def add_song(self, username, title, artist):
        if self.linked_list.tail and len(self.linked_list) == 5:
            print("Playlist is full! You cannot add more songs.")
            return
        song = Song(title, artist)
        self.linked_list.add_node(song)
        user = User(username, '')
        user.playlist = self
        user.save_playlist()

    def remove_song(self, title):
        song = Song(title, "")
        if self.linked_list.remove_node(song):
            print(f"{title} has been removed from the playlist!")
        else:
            print(f"{title} is not in the playlist.")

    def get_song_list(self):
        song_list = []
        if len(self.linked_list) == 0:
            print("The playlist is empty.")
        else:
            for i, song in enumerate(self.linked_list):
                song_list.append(song)
                print(f"{i+1}. {song.title} - {song.artist}")
        return song_list


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.playlist = Playlist()
        
    def __repr__(self):
        return f"User({self.username}), Password({self.password})"
    
    def add_song_to_playlist(self, title, artist):
            self.playlist.add_song(title, artist)
            self.save_playlist()
            print("Added song to playlist")

    def remove_song_from_playlist(self, song_title):
        self.playlist.remove_song(song_title)
        self.save_playlist()
        
    def display_playlist(self):
        for song in self.playlist.linked_list:
            print(f"{song.title} - {song.artist}\n")
    
    def open_playlist(self):
        song_list = []
        with open(f"{self.username}_playlist.txt", "r") as f:
            for line in f:
                title, artist = line.strip().split("-")
                song_list.append(Song(title.strip(), artist.strip()))
        return song_list

    def save_playlist(self):
        with open(f"{self.username}_playlist.txt", "w") as f:
            for song in self.playlist.linked_list:
                f.write(f"{song.title} - {song.artist}\n")
        
        