import praw
import pandas as pd
from sentiment_analysis import predict_sentiment

# Replace with your Reddit API credentials
CLIENT_ID = "1"
CLIENT_SECRET = "1"
USER_AGENT = "1"

# Initialize the Reddit client
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Define subreddits to monitor (you can add more subreddits separated by +)
subreddit = reddit.subreddit("news+worldnews")

# CSV file to store posts and sentiment data
DATA_FILE = "reddit_posts.csv"

def update_data(new_post_title):
    """Process a new Reddit submission title and append the result to the CSV."""
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["post", "sentiment", "confidence"])
    
    sentiment, conf = predict_sentiment(new_post_title)
    label = "Positive" if sentiment == 1 else "Negative"
    new_row = {"post": new_post_title, "sentiment": label, "confidence": conf}
    df = df.append(new_row, ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    print(f"Processed: {new_post_title} | Sentiment: {label} (Confidence: {conf:.2f})")
    return new_row

if __name__ == "__main__":
    print("Starting Reddit stream...")
    for submission in subreddit.stream.submissions(skip_existing=True):
        update_data(submission.title)

