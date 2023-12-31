# airtable_utils.py
#import requests
import os
from airtable import Airtable


# Replace these with your actual Airtable API key and base ID
AIRTABLE_API_KEY = os.environ['API_KEY']
AIRTABLE_BASE_ID = os.environ['BASE_KEY']
AIRTABLE_TABLE_NAME = 'Draft2'

def submit_form_data(name, relation, age, location, grewup, interests, relationship, fic_nonfic, email):
     # Initialize Airtable for the desired table
    table = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, api_key=AIRTABLE_API_KEY)

    # Insert the form data into the Airtable table
    try:
        table.insert({
            "Name": name,
            "Relation": relation,
            "Age": age,
            "Location": location,
            "Grewup": grewup,
            "Interests": interests,
            "Relationship": relationship,
            "Fic_Nonfic": fic_nonfic,
            "Email": email
        })

        return True
    except Exception as e:
        print("Error inserting data into Airtable:", str(e))
        return False
