import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_text(text, task="summarize"):
    """
    Analyzes the given text using OpenAI's GPT model based on the specified task.

    Args:
        text (str): The input text to analyze.
        task (str): The task to perform on the text (e.g., "summarize", "analyze sentiment").

    Returns:
        str: The result of the analysis.
    """
    prompt = f"Please {task} the following text:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content