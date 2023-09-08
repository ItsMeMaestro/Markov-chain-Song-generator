import os
import re
import argparse

def remove_punctuation(text):
    # Remove punctuation using regex + some additional cleaning
    cleaned_text = re.sub(r'[^\w\s]', "", text)
    cleaned_text = re.sub(r'\w+\d+Embed\b', "", cleaned_text)
    cleaned_text = re.sub(r'\w+\d+KEmbed\b', "", cleaned_text)
    return cleaned_text

def add_period(line):
    line = line.strip()  # Remove leading and trailing whitespace
    if not line:
        return ""
    if line[0].isupper():
        line = line[0].lower() + line[1:]
   
    
    line += "."  # Add a dot at the end
    return line

def remove_sentences_in_braces(text):
    # Remove lines containing braces using regex
    cleaned_lines = []
    lines = text.split('\n')
    
    for line in lines:
        if not re.search(r'[\(\)\[\]\{\}]', line):
            cleaned_lines.append(line)
    
    cleaned_text = '\n'.join(cleaned_lines)
    return cleaned_text

def clean_lyrics(artist, num, input_folder="lupa", output_folder="pupa"):
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Construct input and output file paths
    input_file_path = os.path.join(input_folder, f"{artist.replace(' ', '')}_{num}.txt")

    output_file_path = os.path.join(output_folder, f"cleaned_{artist.replace(' ', '')}_{num}.txt")

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    
    # Remove sentences within braces and punctuation
    text_remove_braces = remove_sentences_in_braces(text)
    final_cleaned_text = remove_punctuation(text_remove_braces)
    
    # Add periods at the end of lines
    lines = final_cleaned_text.split('\n')
    final_cleaned_text = '\n'.join([add_period(line) for line in lines])
    
    # Write the cleaned text to the output file
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(final_cleaned_text)
# Example usage:
def main():
    parser = argparse.ArgumentParser(description="Clean and format lyrics.")
    parser.add_argument("artist", help="Name of the artist")
    parser.add_argument("num", type=int, help="Lyrics number")
    parser.add_argument("--input-folder", default="lyrics", help="Input folder path")
    parser.add_argument("--output-folder", default="cleanedLyrics", help="Output folder path")

    args = parser.parse_args()

    clean_lyrics(args.artist, args.num, args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()
