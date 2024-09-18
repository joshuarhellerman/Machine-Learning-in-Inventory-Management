import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from utils import ensure_directory


# Initialize the VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment_vader(data):
    sentiment_scores = []

    for item in data:
        content = item['content']
        # Calculate sentiment score using VADER
        sentiment_score = vader_analyzer.polarity_scores(content)['compound']  # Use compound score

        # Append the result with the date and the ID
        sentiment_scores.append({
            'id': item['id'],  # Reference to post/response ID
            'type': item['type'],
            'sentiment_method': 'VADER',
            'sentiment_score': sentiment_score,
            'date': item['date']  # Include date for matching
        })

    return sentiment_scores


# Ensure directory exists before saving files
def ensure_directory(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


# Store the sentiment data in a CSV, appending to existing files
def store_vader_sentiment(sentiment_data, file_path):
    ensure_directory(file_path)

    df = pd.DataFrame(sentiment_data)

    if not os.path.isfile(f'{file_path}_vader_sentiment.csv'):
        df.to_csv(f'{file_path}_vader_sentiment.csv', index=False, mode='w', header=True)
    else:
        df.to_csv(f'{file_path}_vader_sentiment.csv', index=False, mode='a', header=False)
