import os
from lyricsgenius import Genius
import argparse

"""
Scrapes the lyrics of the artist's songs and saves them to a file.
Artist name will be used to name the output file.(case sensitive)
Song download priority is based on popularity."""
def scrap_lyrics(input_artist, max_songs, token, output_folder="lyrics"):
    # Set up your Genius API client
    genius = Genius(token, timeout=10)
    # Search for the artist
    artist = genius.search_artist(input_artist, max_songs=max_songs, sort="popularity")

    songs = {}
    for song in artist.songs:
        song_title = song.title
        song_lyrics = song.lyrics
        songs[song_title] = song_lyrics

    # Define the folder path to save the lyrics files
    
    os.makedirs(output_folder, exist_ok=True)  # Create the "lyrics" folder if it doesn't exist

    # Replace spaces with underscores and create the output file name
    input_artist = artist.name.replace(" ", "")
    output_file = os.path.join(output_folder, f"{input_artist}_{max_songs}.txt")
    
    with open(output_file, "w", encoding="utf-8") as file:
        for title, lyrics in songs.items():
            file.write(f"{title}\n{lyrics}\n\n")
    
    print(f"All {artist.name} unique songs' lyrics have been saved to '{output_file}'.")

# Example usage:
def main():
    parser = argparse.ArgumentParser(description='Scrap lyrics from Genius.com.')
    parser.add_argument('artist', help='Name of the artist')
    parser.add_argument('num', type=int, help='Lyrics number')
    parser.add_argument('token', help='Genius API token')
    parser.add_argument('--output-folder', default="lyrics", help='Output folder path')
    args = parser.parse_args()
    scrap_lyrics(args.artist, args.num, args.token)
if __name__ == "__main__":
    main()


