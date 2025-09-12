import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def generate_swot_chat(description: str) -> dict:
    """
    Sends the description to OpenRouter LLM and returns structured SWOT.
    """
    prompt = f"""
    You are a business analyst. Generate a structured SWOT analysis in JSON format
    with keys: strengths, weaknesses, opportunities, threats.

    Project description: "{description}"
    """

    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.choices[0].message.content.strip()

        import json
        try:
            swot_json = json.loads(text)
        except Exception:
            # fallback if output isn't valid JSON
            swot_json = {"raw_output": text}

        return swot_json

    except Exception as e:
        if hasattr(e, "http_status") and e.http_status == 429:
            return {"error": "⚠️ API quota exceeded. Try again later."}
        return {"error": f"⚠️ {str(e)}"}
