import requests

from app.core.config import settings


def generate_openai_prompt(prompt: str) -> str:
    """
    Simple client for OpenAi Api request
    """
    with requests.Session() as session:
        response = session.get(
            url='http://generate-api:3000/generate',
        )
        result = response.json()

        return result["message"]
    #time.sleep(5)
    #return "test_77"
