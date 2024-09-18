from transformers import pipeline
import torch
import pandas as pd
import os

# Check if a GPU is available and use it if possible
device = -1  # Force CPU usage (change to 0 if you want to use GPU)

# Initialize the HuggingFace transformer model, optimized for finance
# Here we use 'ProsusAI/finbert' which is a FinBERT model pre-trained on financial data
transformer_analyzer = pipeline(
    'sentiment-analysis',
    model="ProsusAI/finbert",  # A finance-focused transformer model
    device=device  # Specify device (GPU or CPU)
)

def analyze_sentiment_transformer(data):
    sentiment_scores = []

    for item in data:
        content = item['content']

        # Tokenize and truncate the content to the first 512 tokens
        inputs = transformer_analyzer.tokenizer(
            content,
            max_length=512,
            truncation=True,  # Truncate to max_length
            return_tensors='pt'  # Return as PyTorch tensors
        )

        # Calculate sentiment score using transformer model
        with torch.no_grad():  # Disable gradient calculation to save memory
            result = transformer_analyzer.model(**inputs)

        # Extract the label and score
        label = transformer_analyzer.postprocess(result, return_all_scores=False)[0]['label']
        score = transformer_analyzer.postprocess(result, return_all_scores=False)[0]['score']

        # Convert labels to numerical values (-1 for negative, +1 for positive)
        if label == 'negative':
            sentiment_score = -score
        elif label == 'positive':
            sentiment_score = score
        else:
            sentiment_score = 0  # Neutral sentiment if applicable

        # Append the result with the post/response ID, type, and date
        sentiment_scores.append({
            'id': item['id'],
            'type': item['type'],
            'sentiment_method': 'Transformer',
            'sentiment_score': sentiment_score,
            'date': item['date']  # Include date for matching
        })

    return sentiment_scores

# Function to store transformer sentiment data
def store_transformer_sentiment(sentiment_data, csv_path):
    """Store the sentiment data as a CSV file."""
    df = pd.DataFrame(sentiment_data)
    if os.path.exists(csv_path):
        # If file exists, append without overwriting
        df.to_csv(csv_path, mode='a', header=False, index=False)
    else:
        # If file doesn't exist, write with headers
        df.to_csv(csv_path, index=False)
