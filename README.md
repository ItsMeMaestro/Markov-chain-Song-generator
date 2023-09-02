# Markov-chain-Song-generator

This is my university semester project for creating a Markov chain lyrics generator.

## Features

- **Markov-Chain-Based lyrics Generation**: Generate text using Markov chains from the lyrics of any author. Includes lyrics from popular rappers like Eminem, Yelawolf, and Logic.

- **Customizable N-grams**: Configure the length of n-grams. If a new word cannot be generated for the current n-gram, the generator removes the last word to improve results. N-grams longer than 3 not recommended, especially for smaller song databases(less than 100 tracks).

- **Line Length Control**: Customize the length of generated lines.

- **Line Quantity Adjustment**: Specify the number of lines you want to generate text for various applications or projects.

## Dependencies

1. Basic modules: `re`, `os`, `numpy`
2. `lyricsgenius`: Used for parsing song lyrics using an API.
3. `pronouncing`: Used to separate words into phonemes using the Carnegie Mellon Dictionary.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the console application(main.py file).
4. Explore the options for generating text using Markov chains.

# Specification
## **lyricsScrapper.py**
  

### Overview
This Python script scrapes the lyrics of an artist's songs using the Genius API and saves them to a text file. The artist's name is used to name the output file (case sensitive), and song download priority is based on popularity.

### Dependencies
- `os`: Used for file system operations.
- `lyricsgenius`: Used for interacting with the Genius API.

### Usage
1. Set up your Genius API client by providing your API key.
2. Specify the artist's name and the maximum number of songs to download.
3. Run the script.





