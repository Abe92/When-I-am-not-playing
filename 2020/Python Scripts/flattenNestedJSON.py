from pathlib import Path
import json
import pandas as pd

# Setting the number of output
pd.set_option('display.expand_frame_repr', False)

'''
Path to File
'''
file_path = Path(r'D:\_19 Python\GIMAC_2020_DataViz\GeneralTasks-Scripts\Nobel_Prizes.json')

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
laureates: pd.core.frame.DataFrame = pd.json_normalize(data['nobelPrizes'])
# print(laureates)

'''
Save the DataFrame as CSV file
'''
laureates.to_csv('nobel_prizes.csv', sep=',', encoding='utf-8')
