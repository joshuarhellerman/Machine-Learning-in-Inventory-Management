import os
import praw
import config
import pandas as pd
from datetime import datetime

# Initialize Reddit API using PRAW
def init_reddit():
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent=config.REDDIT_USER_AGENT,
    )
    return reddit

# Get posts based on subreddit and keywords
def get_posts(subreddits, keywords):
    reddit = init_reddit()
    collected_posts = []

    for subreddit in subreddits:
        subreddit_instance = reddit.subreddit(subreddit)

        # Iterate through the top new posts
        for submission in subreddit_instance.new(limit=config.POST_LIMIT):
            if any(keyword.lower() in submission.title.lower() or keyword.lower() in submission.selftext.lower() for keyword in keywords):
                post_data = {
                    'id': submission.id,
                    'type': 'post',  # Label as a post
                    'title': submission.title,
                    'content': submission.selftext,
                    'timestamp': submission.created_utc,
                    'date': datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d'),  # Store as date
                    'author': submission.author.name if submission.author else 'Unknown',
                    'url': submission.url,
                    'parent_post_id': None  # Posts do not have a parent post
                }
                collected_posts.append(post_data)

    return collected_posts

# Get responses to a post, limiting to a specific number of indirect responses
def get_responses(post_id, max_responses=4):
    reddit = init_reddit()
    post = reddit.submission(id=post_id)
    post.comments.replace_more(limit=0)  # Remove 'MoreComments' objects

    responses = []
    response_counter = 0

    for top_level_comment in post.comments:
        if response_counter >= max_responses:
            break
        response_data = {
            'id': top_level_comment.id,
            'type': 'response',  # Label as a response
            'title': None,  # Responses don’t have titles
            'content': top_level_comment.body,
            'timestamp': top_level_comment.created_utc,
            'date': datetime.utcfromtimestamp(top_level_comment.created_utc).strftime('%Y-%m-%d'),  # Store as date
            'author': top_level_comment.author.name if top_level_comment.author else 'Unknown',
            'url': None,  # Responses don’t have URLs
            'parent_post_id': post_id  # Reference the post being responded to
        }
        responses.append(response_data)
        response_counter += 1

    return responses

# Ensure directory exists before saving files
def ensure_directory(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# Store the combined post and response data in the same CSV file
def store_combined_data(posts, responses, file_path):
    ensure_directory(file_path)

    # Combine post and response data into one dataframe
    combined_df = pd.DataFrame(posts + responses)

    # Check if the file exists to append or write headers
    if not os.path.isfile(file_path):
        combined_df.to_csv(file_path, index=False, mode='w', header=True)
    else:
        combined_df.to_csv(file_path, index=False, mode='a', header=False)
