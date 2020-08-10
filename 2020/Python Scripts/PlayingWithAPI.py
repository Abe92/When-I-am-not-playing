"""
Author   : Aldy Rasyid Abe
Email    : aldyrabe@gmail.com
Title    : Nobel Prize Winners API Communicator
Purpose  : Python script to pull-and-save API data from Nobel Prize Winners API
Reference: - https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/#disqus_thread
           - https://stackoverflow.com/questions/9170288/pretty-print-json-data-to-a-file-using-python
           - http://swcarpentry.github.io/web-data-python/01-getdata/
"""

import requests
import json

''' 
API Endpoint
'''
url = 'https://api.nobelprize.org/2.0/laureates'

'''
Requesting API server status code
'''
response = requests.get(url)
print(response.status_code)

'''
"Pretty-Printing" the Endpoint
'''
laureates_data = response.json()
print(json.dumps(laureates_data, sort_keys=True, indent=4))

'''
Writing JSON to a file with Pretty-Printing
'''
with open('Nobel_Laureates.json', 'w') as outfile:
    json.dump(laureates_data, outfile, sort_keys=True, indent=4)
