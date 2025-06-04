from celery import Celery
from scraper.reddit_scraper import fetch_reddit_posts
from scraper.twitter_scraper import fetch_tweets
from analyzer import analyze_content

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def analyze_social_media():
    reddit_data = fetch_reddit_posts("artificialintelligence", 5)
    twitter_data = fetch_tweets("AI", 5)
    analyze_content(reddit_data + twitter_data)