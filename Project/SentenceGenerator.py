import pronouncing
import numpy as np
"""
Uses pronouncing library to get array of phonemes.
Since CMU dictionary is limited, some words wont have phonemes by default.
In that case, the first letter is removed and the function is called recursively.

"""
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
"""
Choose word based on the previous n words.
If there is no word that can be chosen, the function is called recursively with n-1"""
def choose_word(word_dict, key, sentence, j, n):
    if n == 0:
        return
    key = sentence[-min(j,n):].copy()
    key.reverse()
    if (tuple(key) in word_dict):
                prev_words = [word for word in word_dict.get(tuple(key), [])]
                # Prevent words that are ending previous sentence in the corpus from being used
                prev_words = [word for word in prev_words if "." not in word]
                if not prev_words:
                    choose_word(word_dict, key, sentence, j, n-1)
                    return
                prev_word = np.random.choice(prev_words)
                sentence.append(prev_word)
    else:
        return
"""
Generates sentences based on the corpus and the word dictionary.
"""
def generate_sentences(sentences, words, n, word_dict, last_words):
    wordToRhyme=""
    for i in range(sentences):
        #Find a word to start the sentence(generation in reversed order)
        eligible_last_words = [word for word in last_words if i % 2 == 0 or check_rhyme(word[:-1], wordToRhyme)]
        #Choode a random word from the list of eligible words
        if(eligible_last_words):
            last_word = np.random.choice(eligible_last_words)
            
            sentence = [last_word]
            wordToRhyme=last_word[:-1]
        else:
            last_word = wordToRhyme
        #Generate the rest of the sentence
        for j in range(1,words):
            choose_word(word_dict, sentence, sentence, j,  n)
            
            
        sentence[-1] = sentence[-1].capitalize()  # Capitalize the first words
        sentence.reverse()  # Reverse the generated words to get the sentence from end to start
        result = ' '.join(sentence)
        print(result)
        if((i+1)%4==0):
            print("\n")


#Example usage:
def main():
    wordToRhyme = "love"
    print(check_rhyme("above", wordToRhyme))

if __name__ == "__main__":
    main()