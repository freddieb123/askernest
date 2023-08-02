
def main():
    import os
    from airtable import Airtable
    import openai
    import re


    # replace with your credentials
    base_key = os.environ['BASE_KEY']
    table_name = 'Draft2'
    api_key = os.environ['API_KEY']

    # initialize Airtable
    airtable = Airtable(base_key, table_name, api_key)

    # Get the latest record
    records = airtable.get_all(maxRecords=1, sort=[('created_time', 'desc')])
    latest_record = records[0]['fields']

    # construct the prompt
    prompt = "My uncle lives in {}. And grew up in {}. He is {} years old. And his interests are {}. I would describe our relationship as {}. \n\nRecommend me 5 books based on this description that I could give him. Make sure the recommendations aren't really obvious. Please provide your recommendations as a Python dictionary, with the book title as the key and the author's name as the value. For example: {{\"To Kill a Mockingbird\": \"Harper Lee\", \"1984\": \"George Orwell\"}}. Remove any other text apart from the dictionary.".format(
    latest_record['Location'],
    latest_record['Age'],
    latest_record['Grewup'],
    latest_record['Interests'],
    latest_record['Relationship']
    )
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
    print(books)

    # Initialize Airtable for 'Recommendations' table
    recommendations_table = Airtable(base_key, 'Recommendations', api_key)

    # Insert books into 'Recommendations' table
    recommendations_table.insert({'Books': books})

    return books

if __name__ == "__main__":
    main()
