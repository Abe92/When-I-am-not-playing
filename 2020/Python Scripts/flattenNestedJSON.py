"""
Author   : Aldy Rasyid Abe
Email    : aldyrabe@gmail.com
Title    : JSON Flattener
Purpose  : Python script to 'flattened' the nested JSON file 
Reference: - https://stackoverflow.com/questions/63337764/python-flattening-the-nested-json-file
"""

from pathlib import Path
import json
import pandas as pd

# Setting the number of output
pd.set_option('display.expand_frame_repr', False)

'''
Path to File
'''
file_path = Path(r'file/path/file_name.json')

'''
Read JSON File
'''
with file_path.open('r', encoding='utf-8') as file_accessed:
    data = json.loads(file_accessed.read())
# print(json.dumps(data, sort_keys=True, indent=4))

'''
Create DataFrame from flatten JSON file
'''
# noinspection PyUnresolvedReferences
laureates: pd.core.frame.DataFrame = pd.json_normalize(data['json_file_header_name'])
# print(laureates)

'''
Save the DataFrame as CSV file
'''
laureates.to_csv('file_name.csv', sep=',', encoding='utf-8')
