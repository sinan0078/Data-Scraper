import typer
from tasks import analyze_social_media

app = typer.Typer()

@app.command()
def harvest():
    \"\"\"Start harvesting social media chaos.\"\"\"
    analyze_social_media.delay()
    print(\"Started background harvesting...\")

if __name__ == \"__main__\":
    app()
