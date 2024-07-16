import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the Airtable personal access token and base ID from environment variables
AIRTABLE_ACCESS_TOKEN = os.getenv('AIRTABLE_ACCESS_TOKEN')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME')

# Debug: Print the environment variables to ensure they are loaded correctly
print("AIRTABLE_ACCESS_TOKEN:", AIRTABLE_ACCESS_TOKEN)
print("AIRTABLE_BASE_ID:", AIRTABLE_BASE_ID)
print("AIRTABLE_TABLE_NAME:", AIRTABLE_TABLE_NAME)
