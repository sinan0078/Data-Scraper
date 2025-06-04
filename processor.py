import re
import emoji

def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\\S+', '', text)
    # Remove mentions and hashtags
    text = re.sub(r'[@#]\\S+', '', text)
    # Remove emojis
    text = emoji.replace_emoji(text, replace='')
    # Remove special characters
    text = re.sub(r'[^A-Za-z0-9\\s]', '', text)
    # Lowercase
    text = text.lower().strip()
    return text

