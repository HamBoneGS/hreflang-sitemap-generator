# takes the hreflang input with Unique URLs, Codes, and "Chunk URLs" and formats correctly

# THIS IS MY GREATEST ACHEIVEMENT

import pandas as pd

input_file = "C:\development\sorter\intuit-for-sorter.csv"
csv_file = pd.read_csv(input_file)
unique_list = csv_file['chunks'].unique()

empty_list = []


for value in unique_list:
    lst = []
    df_1 = csv_file.loc[csv_file['chunks'] == value]
    df_2 = df_1.drop(columns='chunks')
    df_3 = df_2.transpose()
    row = df_3.iloc[0]
    list_1 = []
    for item in row:
        list_1.append(item)
    empty_list.append(list_1)

master_df = pd.DataFrame(empty_list)
print(master_df)

master_df.to_csv("test.csv")

# for row in csv
# copy chunk value
# if chunk value == chunk copy
# append values to row
# if chunk value does not match, pop new value, repeat