
import os
from airtable import Airtable
import openai
import re
import isbnlib
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# replace with your credentials
base_key = os.environ['BASE_KEY']
table_name = 'Draft2'
api_key = os.environ['API_KEY']
AIRTABLE_ACCESS_TOKEN = os.getenv('AIRTABLE_ACCESS_TOKEN')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
TABLE_NAME = 'Draft2'

def get_book_info_from_isbn(isbn_dict):
    books_info = {}
    print(isbn_dict)


    for title, info in isbn_dict.items():
        author, isbn = info

        amazon_link = f"https://www.amazon.co.uk/s?k={title}+{author}"

        # Send request to Google Books API
        url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}"
        response = requests.get(url)
        data = response.json()

        if "items" in data and len(data["items"]) > 0:
            item = data["items"][0]["volumeInfo"]
            authors = item.get("authors", ["Author not found"])
            thumbnail = item.get("imageLinks", {}).get("thumbnail", "")
            books_info[title] = {
                "authors": authors,
                "thumbnail": thumbnail,
                "amazonLink": amazon_link  # Add the Amazon link to the data
            }
        else:
            print(f"Book by {author} not found.")

    return books_info

def main(recommendationType):
     # Construct headers for Airtable API requests
    headers = {
        'Authorization': f'Bearer {AIRTABLE_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    # initialize Airtable
    airtable = Airtable(base_key, table_name, api_key)

     # Get the latest record from Airtable
    url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{TABLE_NAME}?maxRecords=1&sort[0][field]=created_time&sort[0][direction]=desc'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    records = response.json().get('records')
    latest_record = records[0]['fields']
    print("latest")
    print(latest_record)

    # construct the prompt
    if recommendationType == "forYourself":
        prompt = "I am buying a book for myself. I live in {}. And I grew up in {}. I am {} years old. And my interests are {}. I would describe myself in three words as {}. \n\nRecommend me 5 books based on this description. Make sure all the books are {}. Make sure the recommendations aren't really obvious. Please provide your recommendations as a Python dictionary, with the book title as the key and a list containing the author's name and the ISBN number as the value. For example: {{\"To Kill a Mockingbird\": [\"Harper Lee\", \"978-0099549482\"], \"1984\": [\"George Orwell\", \"978-1846975769\"]}}. Remove any other text apart from the dictionary.".format(
        latest_record['Location'],
        latest_record['Grewup'],
        latest_record['Age'],
        latest_record['Interests'],
        latest_record['Relationship'],
        latest_record['Fic_Nonfic'])
    # Customize the rest of the prompt for oneself
    else:
        prompt = "I am buying a book for my {}. They live in {}. And grew up in {}. They are {} years old. And their interests are {}. And for context I would describe our relationship in three words as {}. \n\nRecommend me 5 books based on this description that I could give him. Make sure all the books are {}. Make sure the recommendations aren't really obvious. Please provide your recommendations as a Python dictionary, with the book title as the key and a list containing the author's name and the ISBN number as the value. For example: {{\"To Kill a Mockingbird\": [\"Harper Lee\", \"978-0099549482\"], \"1984\": [\"George Orwell\", \"978-1846975769\"]}}. Remove any other text apart from the dictionary.".format(
        latest_record['Relation'],
        latest_record['Location'],
        latest_record['Grewup'],
        latest_record['Age'],
        latest_record['Interests'],
        latest_record['Relationship'],
        latest_record['Fic_Nonfic'])

    print(prompt)
    # Set your OpenAI key
    openai.api_key = os.environ['OPENAI_KEY']

    # Generate response from the model
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an expert bookseller."},
        {"role": "user", "content": prompt}
      ]
    )
    books = response.choices[0].message.content.strip()
    books=json.loads(books)
    print(books)
    books_google = get_book_info_from_isbn(books)
    print(books_google)
    print(type(books_google))

     # Insert books into 'Recommendations' table in Airtable
    recommendations_table = 'Recommendations'
    recommendations_url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{recommendations_table}'
    books_google_str = json.dumps(books_google)
    data = {
        'fields': {
            'Books': books_google_str
        }
    }
    response = requests.post(recommendations_url, headers=headers, json=data)
    response.raise_for_status()
    print("Books inserted successfully into Recommendations table")

    return books_google

if __name__ == "__main__":
    main()
