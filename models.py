from pydantic import BaseModel

class Post(BaseModel):
    source: str  # reddit or twitter
    original_text: str
    summary: str

class AnalysisRequest(BaseModel):
    platform: str
    keyword: str
    limit: int = 10
