
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
    prompt = f"This description is about my {latest_record['Relationship']}: they grew up in {latest_record['Location']}. They describe themselves in 3 words as {latest_record['Three words']}. Their main interests are {latest_record['What are their main interests?']}. A typical meeting between us looks like {latest_record['Typical meeting']}. And I would describe the conversation as {latest_record['Conversation']}. \n\nFinally, they like {latest_record['Fiction/Non-fiction']} books. \n\nRecommend me 5 books based on this description. Make sure the recommendations aren't really obvious. Provide the response as a Python dictionary with key value pairs being Book title and Explanation respectively."

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
    print("response")
    print(response)
    books = response.choices[0].message.content()
    print(books)
    return books

if __name__ == "__main__":
    main()
