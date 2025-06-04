from gpt_engine import analyze_text
from database import save_result

def analyze_content(posts):
    for content in posts:
        if isinstance(content, tuple):
            content = " ".join(content)
        summary = analyze_text(content)
        save_result({"original": content, "summary": summary})