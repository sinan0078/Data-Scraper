chaos_harvester/
├── main.py                # FastAPI entry point
├── config.py              # Config for API keys, intervals, etc.
├── gpt_engine.py          # OpenAI GPT interaction
├── scraper/
│   ├── reddit_scraper.py  # Reddit scraping logic using PRAW
│   └── twitter_scraper.py # Twitter scraping using snscrape or Tweepy
├── processor.py           # Cleans and prepares text
├── analyzer.py            # GPT-driven analysis
├── tasks.py               # Celery tasks for background jobs
├── scheduler.py           # APScheduler jobs
├── database.py            # MongoDB connector
├── models.py              # Pydantic models
├── cli.py                 # CLI command definitions
├── requirements.txt       # Dependencies
└── .env                   # API keys and environment variables