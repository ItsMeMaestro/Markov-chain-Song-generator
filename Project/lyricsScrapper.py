import os
from lyricsgenius import Genius

# Set up your Genius API client
genius = Genius("Enter token here", timeout=10)
"""
Scrapes the lyrics of the artist's songs and saves them to a file.
Artist name will be used to name the output file.(case sensitive)
Song download priority is based on popularity."""
def scrap_lyrics(input_artist, max_songs):
    # Search for the artist
    artist = genius.search_artist(input_artist, max_songs=max_songs, sort="popularity")

    songs = {}
    for song in artist.songs:
        song_title = song.title
        song_lyrics = song.lyrics
        songs[song_title] = song_lyrics

    # Define the folder path to save the lyrics files
    folder_name = "lyrics"
    os.makedirs(folder_name, exist_ok=True)  # Create the "lyrics" folder if it doesn't exist

    # Replace spaces with underscores and create the output file name
    input_artist = artist.name.replace(" ", "")
    output_file = os.path.join(folder_name, f"{input_artist}_{max_songs}.txt")
    
    with open(output_file, "w", encoding="utf-8") as file:
        for title, lyrics in songs.items():
            file.write(f"{title}\n{lyrics}\n\n")
    
    print(f"All {artist.name} unique songs' lyrics have been saved to '{output_file}'.")

# Example usage:
def main():
    artist_name = "Taylor Swift"
    max_songs = 10
    scrap_lyrics(artist_name, max_songs)

if __name__ == "__main__":
    main()

