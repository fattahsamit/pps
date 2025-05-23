liked_songs = {
    "Numb": "Linkin Park",
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Reptilia": "The Strokes"
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write("Liked Songs:\n")
        for song, artist in liked_songs.items():
            file.write(f"{song} by {artist}\n")
            

file_name = "liked_songs.txt"
write_liked_songs_to_file(liked_songs, file_name)