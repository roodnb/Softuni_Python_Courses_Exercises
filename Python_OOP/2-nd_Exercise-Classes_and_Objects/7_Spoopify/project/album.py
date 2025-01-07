from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        try:
            current_song = [sng for sng in self.songs if sng.name == song_name][0]
            self.songs.remove(current_song)
            return f"Removed song {song_name} from album {self.name}."
        except IndexError:
            return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        for sng in self.songs:
            result += f"== {sng.get_info()}\n"
        return result

