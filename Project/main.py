from lyricsScrapper import scrap_lyrics
from lyricsCleaner import clean_lyrics
import chainBuilder
import SentenceGenerator
import os
"""
This program generates random sentences based on the lyrics of a given artist.
"""
"""
The function below reads settings from a file and returns them as a dictionary.
"""
def read_settings(filename):
    settings = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                settings[key] = value
    except FileNotFoundError:
        pass  # Handle the case when the settings file doesn't exist
    return settings

"""
The function below saves settings to a file.
"""
def save_settings(filename, settings):
    with open(filename, 'w') as file:
        for key, value in settings.items():
            file.write(f"{key}: {value}\n")

# Function to display current settings
def display_settings(settings):
    print("Current Settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")
"""
Gets artist name(as written in the file name) and returns a list of possible song numbers
"""
def find_possible_artist_names():
    folder_path = "cleanedLyrics"
    artist_names = []

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        # Check if the filename ends with ".txt"
        if filename.endswith(".txt"):
            # Extract the artist name from the filename
            artist_name = filename.split("_")[1]
            artist_names.append(artist_name)
    return artist_names
def find_possible_song_numbers(artist_name):
    folder_path = "cleanedLyrics"
    artist_name = artist_name.replace(" ", "_")
    artist_name = artist_name.replace("cleaned_", "")
    print(artist_name)
    song_numbers = []

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        # Check if the filename contains the artist's name and ends with ".txt"
        if artist_name in filename and filename.endswith(".txt"):
            # Extract the song number from the filename
            try:
                
                filename = filename.replace(".", "_")
                song_number = int(filename.split("_")[-2])
                song_numbers.append(song_number)
            except ValueError:
                continue  # Skip filenames that don't have a valid song number

    return song_numbers
# Read settings from the file
settings_filename = 'settings.txt'
settings = read_settings(settings_filename)

# Check if other settings exist, and if not, prompt the user to enter them
if 'ngram_length' not in settings:
    print("Enter number of words in n-gram:")
    k = int(input())
    settings['ngram_length'] = str(k)
    save_settings(settings_filename, settings)

if 'words_in_sentence' not in settings:
    print("Enter number of words in a sentence:")
    words_in_sentence = int(input())
    settings['words_in_sentence'] = str(words_in_sentence)
    save_settings(settings_filename, settings)

if 'num_sentences' not in settings:
    print("Enter number of sentences:")
    num_sentences = int(input())
    settings['num_sentences'] = str(num_sentences)
    save_settings(settings_filename, settings)
if 'token' not in settings:
    print("Enter Genius token:")
    token = input()
    settings['token'] = str(token)
    save_settings(settings_filename, settings)
while True:
    # Display the current settings and options
    display_settings(settings)
    print("Options:")
    print("1. Change settings")
    print("2. Continue with the program")
    print("3. Add new artist")
    print("4. Change Genius token")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Display the current settings and options
        print("Options:")
        print("a. Change n-gram length")
        print("b. Change words in a sentence")
        print("c. Change number of sentences")
        print("d. Go back to the main menu")
        sub_choice = input("Enter your choice: ")
        # Change the settings based on the user's choice
        if sub_choice == "a":
            print("Enter new n-gram length:")
            k = int(input())
            settings['ngram_length'] = str(k)
            save_settings(settings_filename, settings)
        elif sub_choice == "b":
            print("Enter new number of words in a sentence:")
            words_in_sentence = int(input())
            settings['words_in_sentence'] = str(words_in_sentence)
            save_settings(settings_filename, settings)
        elif sub_choice == "c":
            print("Enter new number of sentences:")
            num_sentences = int(input())
            settings['num_sentences'] = str(num_sentences)
            save_settings(settings_filename, settings)
        elif sub_choice == "d":
            continue
    elif choice == "2":
        #Proceed with the program
        possible_artists = find_possible_artist_names()
        previous_artists = []
        for artist in possible_artists:
            if(artist not in previous_artists):
                print(find_possible_song_numbers(artist))
                previous_artists.append(artist)
            

        print("Enter artist name:")
        artist = input()
        possible_song_numbers = find_possible_song_numbers(artist)
        
        if not possible_song_numbers:
            print(f"No cleaned lyrics files found for {artist}.")
            continue
        else: 
            print(f"Possible song numbers for {artist} are: {possible_song_numbers}")
            print("Enter number of songs:")
            songs = int(input())
        if songs not in possible_song_numbers:
            print(f"Invalid song number. Possible song numbers are: {possible_song_numbers}")
            continue
        k = int(settings['ngram_length'])
        sentences = int(settings['num_sentences'])
        words = int(settings['words_in_sentence'])

        corpus = chainBuilder.load_cleaned_lyrics(artist, songs)
        
        word_dict, last_words = chainBuilder.create_word_dict(k, corpus)
        SentenceGenerator.generate_sentences(sentences, words, k, word_dict, last_words)
        break
    elif choice == "3":
        #Add new artist and download lyrics
        print("Enter artist name:")
        artist = input()
        print("Enter number of songs:")
        max_songs = int(input())
        scrap_lyrics(artist, max_songs, settings['token'])
        clean_lyrics(artist, max_songs, "lyrics", "cleanedLyrics")
        break
    elif choice == "4":
        #Change Genius token
        print("Enter new Genius token:")
        token = input()
        settings['token'] = str(token)
        save_settings(settings_filename, settings)
        break
    elif choice == "5":
        #Exit
        break

