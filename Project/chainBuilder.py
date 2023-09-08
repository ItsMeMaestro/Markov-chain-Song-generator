"""
As the script just builds Markov chains in RAM, it does not require main() function. 
"""
import os
#Create ngrams
def ngram_generator(corpus,n ):
    for i in range(len(corpus) - n):
        sublist = corpus[i+1:i+n+1].copy()  # Create a copy of the sublist
        sublist.append(corpus[i])  # First word of the n-gram will be the value in the dictionary
        yield (tuple(sublist))
"""
Loads lyrics from a file and returns a list of words."""
def load_cleaned_lyrics(artist, max_songs):
    input_folder = "cleanedLyrics"
    input_file_path = os.path.join(input_folder, f"cleaned_{artist}_{max_songs}.txt")
    text = open(input_file_path, encoding='utf8').read()
    corpus = text.split()
    return corpus

"""
Creates a dictionary of n-grams from the corpus.
Key entries in dictionary will be of 1 to n length.(All possible n-grams,n-1-grams,...,1-gram)
"""
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
    last_words = []
    for i in range(len(corpus)):
        if corpus[i] and corpus[i][-1] == '.':
            last_words.append(corpus[i])
    return word_dict, last_words


    


