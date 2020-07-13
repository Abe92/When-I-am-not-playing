import pandas as pd
import os
import missingno as msno
import matplotlib.pyplot as plt

# Pandas setting to display output messages maximum rows
pd.options.display.max_rows = 500

# Load file; in this case a CSV file from Oxford Uni on DD/MM/YY
# Syntax: df = pd.read_csv('file/path/file_name.csv')
df = pd.read_csv('D:/_00 UN Volunteers/22 June - Ongoing/Oxford Uni Dataset/07-20/OxCGRT_09-7-20.csv')
file_name = os.path.basename('D:/_00 UN Volunteers/22 June - Ongoing/Oxford Uni Dataset/09-20/OxCGRT_13-7-20.csv')

# Counting NaNs inside the DataFrame
# Syntax: count=df.isna().sum()
#         print("NaNs count for this DataFrame is: " + str(count))
count = df.isna().sum()
print("The DataFrame is using " + file_name)
print("NaN counts for this DataFrame is:\n" + str(count))

msno.bar(df.drop('CountryName', axis='columns').sample(500))
plt.show()
