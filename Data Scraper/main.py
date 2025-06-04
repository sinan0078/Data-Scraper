from fastapi import FastAPI
from tasks import analyze_social_media
from scheduler import start_scheduler
start_scheduler()

app = FastAPI()

@app.get("/run-analysis")
def run_analysis():
    analyze_social_media.delay()
    return {"status": "Analysis started in background"}