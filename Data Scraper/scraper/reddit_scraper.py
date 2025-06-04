import praw
from config import REDDIT_CLIENT_ID, REDDIT_SECRET

def fetch_reddit_posts(subreddit_name, limit=10):
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                         client_secret=REDDIT_SECRET,
                         user_agent="chaosHarvester")
    subreddit = reddit.subreddit(subreddit_name)
    return [(post.title, post.selftext) for post in subreddit.hot(limit=limit)]