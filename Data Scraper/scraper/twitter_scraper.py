import snscrape.modules.twitter as sntwitter

def fetch_tweets(query, limit=10):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
        tweets.append(tweet.content)
    return tweets