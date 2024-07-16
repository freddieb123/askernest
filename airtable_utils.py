# airtable_utils.py
#import requests
import os
from airtable import Airtable
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()


# Replace these with your actual Airtable API key and base ID
AIRTABLE_ACCESS_TOKEN = os.getenv('AIRTABLE_ACCESS_TOKEN')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME')

print("AIRTABLE_ACCESS_TOKEN:", AIRTABLE_ACCESS_TOKEN)


def submit_form_data(name, relation, age, location, grewup, interests, relationship, fic_nonfic, email):
    url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    headers = {
        'Authorization': f'Bearer {AIRTABLE_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
    "fields": {
            "Name": name,
            "Relation": relation,
            "Age": age,
            "Location": location,
            "Grewup": grewup,
            "Interests": interests,
            "Relationship": relationship,
            "Fic_Nonfic": fic_nonfic,
            "Email": email
        }
    }
    print(url,headers,data)
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred:", str(http_err))
        return False
    except Exception as e:
        print("Error inserting data into Airtable:", str(e))
        return False
