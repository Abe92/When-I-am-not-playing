import pandas as pd
import os

# Pandas setting to display out messages
pd.set_option('display.max_column', None)
pd.set_option('display.width', 200)

# Load files --- 1
file1 = pd.read_excel('file/path/file_name.xls')
file_name1 = os.path.basename('file/path/file_name.xls')

# Counting NaNs inside the DataFrame --- 1
count1 = file1.isna().sum()
print("The DataFrame1 is using " + file_name1)
print("NaN counts for this DataFrame1 is:\n" + str(count1) + "\n")

# Load files --- 2
file2 = pd.read_excel('file/path/file_name.xls')
file_name2 = os.path.basename('file/path/file_name.xls')

# Counting NaNs inside the DataFrame --- 2
count2 = file2.isna().sum()
print("The DataFrame2 is using " + file_name2)
print("NaN counts for this DataFrame2 is:\n" + str(count2))
