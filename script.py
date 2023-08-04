
import os
from airtable import Airtable
import openai
import re
import isbnlib
import requests
import json


# replace with your credentials
base_key = os.environ['BASE_KEY']
table_name = 'Draft2'
api_key = os.environ['API_KEY']

def get_book_info_from_isbn(isbn_dict):
    books_info = {}

    for title, isbn in isbn_dict.items():
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
                "thumbnail": thumbnail
            }
        else:
            print(f"Book with ISBN {isbn} not found.")

    return books_info

def main():

    # initialize Airtable
    airtable = Airtable(base_key, table_name, api_key)

    # Get the latest record
    records = airtable.get_all(maxRecords=1, sort=[('created_time', 'desc')])
    latest_record = records[0]['fields']
    print("latest")
    print(latest_record)

    # construct the prompt
    prompt = "I am buying a book for my {}. They live in {}. And grew up in {}. They are {} years old. And their interests are {}. And for context I would describe our relationship in three words as {}. \n\nRecommend me 5 books based on this description that I could give him. Make sure all the books are {}. Make sure the recommendations aren't really obvious. Please provide your recommendations as a Python dictionary, with the book title as the key and the author's name as the value. For example: {{\"To Kill a Mockingbird\": \"Harper Lee\", \"1984\": \"George Orwell\"}}. Remove any other text apart from the dictionary.".format(
    latest_record['Relation'],
    latest_record['Location'],
    latest_record['Grewup'],
    latest_record['Age'],
    latest_record['Interests'],
    latest_record['Relationship'],
    latest_record['Fic_Nonfic']
    )
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

    # Initialize Airtable for 'Recommendations' table
    recommendations_table = Airtable(base_key, 'Recommendations', api_key)

    # Insert books into 'Recommendations' table
    books_google_str = json.dumps(books_google)
    recommendations_table.insert({'Books': books_google_str})

    return books_google

if __name__ == "__main__":
    main()
