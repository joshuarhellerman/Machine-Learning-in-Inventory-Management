import os
import pandas as pd
from textblob import TextBlob
from utils import ensure_directory



def analyze_sentiment_textblob(data):
    sentiment_scores = []

    for item in data:
        content = item['content']
        # Calculate sentiment score using TextBlob
        blob = TextBlob(content)
        sentiment_score = blob.sentiment.polarity  # Polarity score from -1 to 1

        # Append the result with the date and the ID
        sentiment_scores.append({
            'id': item['id'],  # Reference to post/response ID
            'type': item['type'],
            'sentiment_method': 'TextBlob',
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
def store_textblob_sentiment(sentiment_data, file_path):
    ensure_directory(file_path)

    df = pd.DataFrame(sentiment_data)

    if not os.path.isfile(f'{file_path}_textblob_sentiment.csv'):
        df.to_csv(f'{file_path}_textblob_sentiment.csv', index=False, mode='w', header=True)
    else:
        df.to_csv(f'{file_path}_textblob_sentiment.csv', index=False, mode='a', header=False)
