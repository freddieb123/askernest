
def results():
    import os
    from airtable import Airtable
    import openai
    import re


    # replace with your credentials
    base_key = os.environ['BASE_KEY']
    table_name = 'Recommendations'
    api_key = os.environ['API_KEY']

    # initialize Airtable
    airtable = Airtable(base_key, table_name, api_key)

    # Get the latest record
    records = airtable.get_all(maxRecords=1, sort=[('created_time', 'desc')])
    latest_record = records[0]['fields']

    print(type(latest_record))
    return latest_record

if __name__ == "__main__":
    results()
