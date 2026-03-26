import pandas as pd
import os
import numpy as np

df = pd.read_csv("pandasModule/liverPatients.csv", names=['Age', 'Gender', 'TB', 'DB', 'Alkphos', 'Sgpt', 'Sgot', 'TP', 'ALB', 'A/G Ration'], index_col=False)
# print(df.head())
# print(df.info())
# print(df.describe)
# print(df.describe())
# print(df.size) # gives the count of rows in datafram
# print(df.shape) # returns the count of rows and columns
# print(list(df.keys())) #returns column names and list(df.keys()) converts column names to list
# print(df.columns) # returns column names
# print(f" Minimum Value from List of TB is : {min(df['TB'].to_list())}")
# print(f" Minimum Value from df of TB is : {min(df['TB'])}")

# print(f" Maximum Value from List of TB is : {max(df['TB'].to_list())}")
# print(f" Maximum Value from df of TB is : {max(df['TB'])}")

# print(f" Mean Value from List of TB is : {np.mean(df['TB'].to_list())}")
# print(f" Maen Value from df of TB is : {np.mean(df['TB'])}")

# print(f" Maximum Value from List of TB is : {np.median(df['TB'].to_list())}")
# print(f" Median Value from df of TB is : {np.median(df['TB'])}")

print(df["Gender"].value_counts())
# print(df)
genderCat = pd.cut(df['Gender'], bins=['Male', 'Female'], labels=[1,2])
print(genderCat)

