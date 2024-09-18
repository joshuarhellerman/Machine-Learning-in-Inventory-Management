import time
import sys
import config
from data_collection.reddit import get_posts, get_responses
from sentiment_analysis.vader import analyze_sentiment_vader, store_vader_sentiment
from sentiment_analysis.textblob import analyze_sentiment_textblob, store_textblob_sentiment
from sentiment_analysis.transformer import analyze_sentiment_transformer, store_transformer_sentiment

def print_live_update(message):
    """Prints live updates in the same line."""
    sys.stdout.write("\r" + message)
    sys.stdout.flush()


def run_tool():
    while True:
        print("Collecting data and calculating sentiment scores...")

        # Step 1: Load Config
        subreddits = config.SUBREDDITS
        keywords = config.KEYWORDS

        # Step 2: Data Collection
        posts = get_posts(subreddits, keywords)
        responses = []

        # Check if there are any new posts
        if len(posts) > 0:
            for post in posts:
                responses += get_responses(post['id'], config.MAX_RESPONSES)

            # Combine posts and responses for sentiment analysis
            data = posts + responses

            # Step 3: Sentiment Analysis using VADER
            vader_sentiment_data = analyze_sentiment_vader(data)
            store_vader_sentiment(vader_sentiment_data, 'data/sentiment_vader.csv')

            # Step 4: Sentiment Analysis using TextBlob
            textblob_sentiment_data = analyze_sentiment_textblob(data)
            store_textblob_sentiment(textblob_sentiment_data, 'data/sentiment_textblob.csv')

            # Step 5: Sentiment Analysis using Transformer
            transformer_sentiment_data = analyze_sentiment_transformer(data)
            store_transformer_sentiment(transformer_sentiment_data, 'data/sentiment_transformer.csv')

            print(f"Processed {len(posts)} new posts and {len(responses)} responses.")
        else:
            print("No new posts found during this interval.")

        # Step 6: Sleep for a defined period before collecting new data
        print(f"Sleeping for {config.CHECK_INTERVAL} seconds...")
        time.sleep(config.CHECK_INTERVAL)


if __name__ == "__main__":
    run_tool()
