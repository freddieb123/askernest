import os
from airtable import Airtable
import openai

# replace with your credentials
base_key = 'app7bZnZImP7X9qDI'
table_name = 'Draft'
api_key = 'keyTTV2pwUhoGhicb'

# initialize Airtable
airtable = Airtable(base_key, table_name, api_key)

def main():
    # Get the latest record
    records = airtable.get_all(maxRecords=1)
    latest_record = records[0]['fields']

    # construct the prompt
    prompt = f"This description is about my {latest_record['Relation']}: they grew up in {latest_record['Location']}. They describe themselves in 3 words as {latest_record['Three words']}. Their main interests are {latest_record['What are their main interests?']}. A typical meeting between us looks like {latest_record['Typical meeting']}. And I would describe the conversation as {latest_record['Conversation']}. \n\nFinally, they like {latest_record['Fiction/Non-fiction']} books. \n\nRecommend me 5 books based on this description. Make sure the recommendations aren't really obvious. "

    # Set your OpenAI key
    openai.api_key = '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'

    # Generate response from the model
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an expert bookseller."},
        {"role": "user", "content": prompt}
      ]
    )
    print(response)
    print(response.choices[0].message.content.strip())

if __name__ == "__main__":
    main()
