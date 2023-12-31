
def results():
    import os
    from airtable import Airtable
    import openai
    import re
    import json


    # replace with your credentials
    base_key = os.environ['BASE_KEY']
    table_name = 'Recommendations'
    api_key = os.environ['API_KEY']

    # initialize Airtable
    airtable = Airtable(base_key, table_name, api_key)

    # Get the latest record
    records = airtable.get_all(maxRecords=1, sort=[('created_time', 'desc')])
    latest_record = records[0]['fields']
    print("raw")
    print(latest_record)
    booklist_str = next(iter(latest_record.values()))
    print(booklist_str)
    booklist_str = booklist_str.replace("'", '"')
    print(booklist_str)

    booklist_dict = json.loads(booklist_str)
    print("dict")
    print(booklist_dict)
    return booklist_dict

if __name__ == "__main__":
    results()
