# Markov-chain-Song-generator

This is my university semester project for creating a Markov chain lyrics generator.

## Features

- **Lyrics-Based Text Generation**: Generate text using Markov chains from the lyrics of any author. Includes lyrics from popular rappers like Eminem, Yelawolf, and Logic.

- **Customizable N-grams**: Configure the length of n-grams for text generation. If a new word cannot be generated for the current n-gram, the generator intelligently removes the last word to improve results.

- **Line Length Control**: Customize the length of generated lines to fit your preferred style or context.

- **Line Quantity Adjustment**: Specify the number of lines you want to generate text for various applications or projects.

## Dependencies

1. Basic modules: `re`, `os`, `numpy`
2. `lyricsgenius`: Used for parsing song lyrics using an API.
3. `pronouncing`: Used to separate words into phonemes using the Carnegie Mellon Dictionary.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run the console application.
4. Explore the options for generating text using Markov chains.



