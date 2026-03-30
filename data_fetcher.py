import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    Holt die Tierdaten für 'animal_name' von der API.
    Gibt eine Liste von Tieren (Dictionaries) zurück.
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': API_KEY}

    response = requests.get(api_url, headers=headers)

    # Wandelt die Antwort direkt in nutzbare Daten um und gibt sie zurück
    return response.json()