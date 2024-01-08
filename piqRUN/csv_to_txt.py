# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:15:20 2023

@author: salva
"""

import pandas as pd
import os

inpt = input('please input the file name abbrev.: ')
df1 = input('please input detector A file name: ')
df2 = input('please input detector B file name: ')

detA = pd.read_csv(df1, header=0)
detB = pd.read_csv(df2, header=0)

# Make sure that the DataFrames have the same number of rows
if len(detA) != len(detB):
    raise ValueError("ERROR: detA and detB must have the same number of rows")
    
# Iterate through both DataFrames row by row
for index in range(len(detA)):
    rowA = detA.iloc[index]
    rowB = detB.iloc[index]
    rowA = rowA.values
    rowB = rowB.values
    
    with open(str(inpt) + f'shot_{index}.txt', 'w') as file:
        for x1, x2 in zip(rowA, rowB):
            # Write the elements separated by a comma and a space
            file.write(f'{x1}, {x2}\n')
            


    
    
    