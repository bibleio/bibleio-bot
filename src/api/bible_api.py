import requests
from dotenv import load_dotenv
import os


def call_bible_api(endpoint):
    try:
        url = f"https://api.scripture.api.bible/v1/{endpoint}"
        headers = {'api-key': os.getenv("API_KEY")}
        response = requests.get(url, headers=headers)

        response.raise_for_status()

        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
