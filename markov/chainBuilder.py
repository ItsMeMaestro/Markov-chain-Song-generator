import numpy as np
import pronouncing
import os
import re
k=4
def check_rhyme(word1, word2):
    phonetics1 = pronouncing.phones_for_word(word1)
    phonetics2 = pronouncing.phones_for_word(word2)

    # Check if phonetics are not present for word1
    while not phonetics1:
        # Remove the first letter from word1 and try again
        word1 = word1[1:]
        phonetics1 = pronouncing.phones_for_word(word1)
        
        # If word1 is empty, return False
        if not word1:
            return False

    # Check if phonetics are not present for word2
    while not phonetics2:
        # Remove the first letter from word2 and try again
        word2 = word2[1:]
        phonetics2 = pronouncing.phones_for_word(word2)
        
        # If word2 is empty, return False
        if not word2:
            return False

    # Compare all possible variants of phonemes for both words
    for phoneme1 in phonetics1:
        for phoneme2 in phonetics2:
            phonemes1 = phoneme1.split()
            phonemes2 = phoneme2.split()
            last_phoneme1 = phonemes1[-1]
            last_phoneme2 = phonemes2[-1]

            if last_phoneme1 == last_phoneme2:
                return True

    return False
#Create ngrams
def ngram_generator(corpus,n ):
    for i in range(len(corpus) - n):
        sublist = corpus[i+1:i+n+1].copy()  # Create a copy of the sublist
        sublist.append(corpus[i])  # First word of the n-gram will be the value in the dictionary
        yield (tuple(sublist))
#Load cleaned lyrics
def load_cleaned_lyrics(artist, max_songs):
    input_folder = "cleanedLyrics"
    input_file_path = os.path.join(input_folder, f"cleaned_{artist}_{max_songs}.txt")
    text = open(input_file_path, encoding='utf8').read()
    corpus = text.split()
    return corpus


def create_word_dict(n, corpus):
    word_dict = {}
    for i in range(n):
        key_length = i+1
        for word_list in ngram_generator(corpus, key_length):
            key = tuple(word_list[:key_length])
            if key in word_dict:
                word_dict[key].append(word_list[-1])
            else:
                word_dict[key] = [word_list[-1]]
    return word_dict
def main():
    corpus = load_cleaned_lyrics("Eminem")
    last_words = []
    for i in range(len(corpus)):
        if corpus[i] and corpus[i][-1] == '.':
            last_words.append(corpus[i])
    word_dict = create_word_dict(k)


    


