# SentimentAnalysis

This repository contains a Python script for performing sentiment analysis on a list of sentences using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the `nltk` library.

## Requirements

- Python 3.x
- `nltk` library
- `pandas` library

## Setup

1. Clone the repository or download the script.
2. Install the required Python libraries using `pip`:

   ```bash
   pip install nltk pandas

 ## Output
The script prints the sentiment analysis results to the console and saves them to a CSV file named sentiment_results.csv.

The output DataFrame contains the following columns:

neg: The percentage of negative words in the sentence.
neu: The percentage of neutral words in the sentence.
pos: The percentage of positive words in the sentence.
compound: The overall sentiment score, ranging from -1 (extremely negative) to +1 (extremely positive).
