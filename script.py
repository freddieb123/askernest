
def main():
    import os
    from airtable import Airtable
    import openai
    import re


    # replace with your credentials
    base_key = os.environ['BASE_KEY']
    table_name = 'Draft'
    api_key = os.environ['API_KEY']

    # initialize Airtable
    airtable = Airtable(base_key, table_name, api_key)

    # Get the latest record
    records = airtable.get_all(maxRecords=1, sort=[('created_time', 'desc')])
    latest_record = records[0]['fields']

    # construct the prompt
    prompt = "This description is about my {}: they grew up in {}. They describe themselves in 3 words as {}. Their main interests are {}. A typical meeting between us looks like {}. And I would describe the conversation as {}. \n\nFinally, they like {} books. \n\nRecommend me 5 books based on this description. Make sure the recommendations aren't really obvious. Please provide your recommendations as a Python dictionary, with the book title as the key and the author's name as the value. For example: {{\"To Kill a Mockingbird\": \"Harper Lee\", \"1984\": \"George Orwell\"}}.".format(
    latest_record['Relationship'],
    latest_record['Location'],
    latest_record['Three words'],
    latest_record['What are their main interests?'],
    latest_record['Typical meeting'],
    latest_record['Conversation'],
    latest_record['Fiction/Non-fiction']
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

    # Initialize Airtable for 'Recommendations' table
    recommendations_table = Airtable(base_key, 'Recommendations', api_key)

    # Insert books into 'Recommendations' table
    recommendations_table.insert({'Books': books})

    return books

if __name__ == "__main__":
    main()
