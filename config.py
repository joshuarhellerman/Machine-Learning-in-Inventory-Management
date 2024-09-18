# Reddit API credentials
REDDIT_CLIENT_ID = 'HV1qR_ppGpNhq8cEou2weA'
REDDIT_CLIENT_SECRET = 'S4Q-yOUdaoE00XhU_1f8pj2getKdhQ'
REDDIT_USER_AGENT = 'Sentiment Miner (by /u/bsjosh)'

# Data collection settings
SUBREDDITS = ['Bitcoin', 'Cryptocurrency']  # Subreddits to monitor
KEYWORDS = ['xrp', 'ripple', 'blockchain']  # Keywords to filter posts
POST_LIMIT = 10  # Maximum number of posts to collect per subreddit

# Maximum number of responses to collect per post
MAX_RESPONSES = 3

# File paths for data storage (adjust this to your preferred location)
# Use relative paths if saving in the project folder
POSTS_CSV_PATH = 'data/posts.csv'  # Combined post and response data

# Interval to check for new posts (in seconds)
CHECK_INTERVAL = 60  # Set to 5 minutes (300 seconds) or any preferred value

