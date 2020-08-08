"""
Author   : Aldy Rasyid Abe
Email    : aldyrabe@gmail.com
Title    : Nobel Prize Winners API Communicator
Purpose  : Python script to pull-and-save API data from Nobel Prize Winners API
Reference: - https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/#disqus_thread
           - https://stackoverflow.com/questions/9170288/pretty-print-json-data-to-a-file-using-python
"""

import requests
import json

''' 
API Endpoint
'''
url = 'https://api.nobelprize.org/2.0/laureates'

'''
Requesting API server status code
note:
- 200, OK, The request has succeeded
- 204, NO Content, The server has completed the request; but doesn't need to return any data
- 400, Bad Request, The request is bad
- 401, Unauthorized, The request requires authentication
- 404, Not Found, The requested resource could not be found
- 408, Timeout, The server gave up waiting for the client
- 418, I'm a teapot, No; really...
- 500, Internal Server Error, An error occurred in the server
'''
response = requests.get(url)
laureates_data = response.json()
print(response.status_code)

'''
"Pretty-Printing"
Print the JSON file into human readable (also known as 'pretty-printing')
add 'sort_keys=True' and 'indent=4'
'''
print(json.dumps(laureates_data, sort_keys=True, indent=4))

'''
Writing JSON to a file with Pretty-Printing
'''
text_file = 'Nobel_Laureates.txt'
json_file = 'Nobel_Laureates.json'

with open('file_name\use\predefined\variables\above', 'w') as outfile:
    json.dump(laureates_data, outfile, sort_keys=True, indent=4)
