from apscheduler.schedulers.background import BackgroundScheduler
from tasks import analyze_social_media

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(analyze_social_media.delay, 'interval', minutes=15)  # Every 15 minutes
    scheduler.start()
