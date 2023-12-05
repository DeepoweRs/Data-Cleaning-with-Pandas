""" 
What should I do with this table?

1. I will delete all duplicates. This will give me a more accurate and efficient table.

2. I will drop a column named "Not_Useful_Column."

3. I will delete all NaN items because I don't need them, and they make the table more confusing.

4. I will fix some names that are written incorrectly in the First_Name and Last_Name columns.

5. I will fix the Phone_Number column because there are many spelling errors there.

6. I will edit the Paying_Customer and Do_Not_Contact columns because the responses are not written in the same way.

7. I will filter the table in different ways. This helps to understand the dataset and analyze it better.

8. Reindex items in the table so that I can understand and analyze the variables better.


Important: You need to change the data location in the code according to where your data located in your PC.

"""


import pandas as pd

tb = pd.read_excel(r'/Users/bedirhankurt/Desktop/Programming/Data Analaysis Project (YFF 2)/Arbeid Delen/Customer Call List.xlsx')
tb.drop_duplicates(inplace = True)
tb = tb.drop(columns = "Not_Useful_Column")
tb.dropna(inplace = True, axis = 0)
tb.loc[16, "First_Name"] = "Micheal"
tb.loc[14, "Last_Name"] = "Flenderson"
tb["Phone_Number"] = tb["Phone_Number"].replace(to_replace = r'\D', value = "-", regex = True)
tb['Paying Customer'] = tb['Paying Customer'].replace({'Y': 'Yes', 'N': 'No'})
tb['Do_Not_Contact'] = tb['Do_Not_Contact'].replace({'Y': 'Yes', 'N': 'No'})
tb = tb[tb["Do_Not_Contact"] == "No"]
tb = tb.reset_index()
tb = tb.drop(columns=['index'])

print(tb.to_string())