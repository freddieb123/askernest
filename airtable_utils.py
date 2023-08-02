# airtable_utils.py
import requests
import os
from airtable import Airtable


# Replace these with your actual Airtable API key and base ID
AIRTABLE_API_KEY = os.environ['API_KEY']
AIRTABLE_BASE_ID = os.environ['BASE_KEY']
AIRTABLE_TABLE_NAME = 'Draft2'

def submit_form_data(name, age, location, interests):
    # Airtable API endpoint
    #url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    #headers = {
        #"Authorization": f"Bearer {AIRTABLE_API_KEY}",
        #"Content-Type": "application/json"
    #}
    payload = {
        "records": [
            {
                "fields": {
                    "Name": name,
                    "Age": age,
                    "Location": location,
                    "Interests": interests
                }
            }
        ]
    }

    # Initialize Airtable for 'responses' table
    responses_table = Airtable(base_key, 'Draft2', AIRTABLE_API_KEY)

    # Insert books into 'responses' table
    responses_table.insert({'Name': name})

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Check for any HTTP error
        return True
    except requests.exceptions.RequestException as e:
        return False
