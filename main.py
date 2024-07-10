# Import necessary libraries
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

# Download necessary resources from nltk
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment of a sentence
def analyze_sentiment(sentence):
    score = sia.polarity_scores(sentence)
    return score

# Example sentences to analyze
sentences = [
    "I love this product, it is fantastic!",
    "I hate this service, it's terrible.",
    "It's an average movie, neither good nor bad.",
    "It was a wonderful day.",
    "I am really disappointed with this experience."
]

# Analyze the sentiments of the sentences
results = [analyze_sentiment(sentence) for sentence in sentences]

# Create a DataFrame to display the results
df_results = pd.DataFrame(results, index=sentences)
print(df_results)

# Save the results to a CSV file
df_results.to_csv('sentiment_results.csv')
