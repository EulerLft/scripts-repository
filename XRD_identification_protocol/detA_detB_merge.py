# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 08:59:13 2024

@author: salva
"""

import pandas as pd 

inpt1 = input('please input DetA file: ')
inpt2 = input('please input DetB file: ')
inpt3 = input('Please input outputfile name: ')

df_A = pd.read_csv(inpt1)
df_B = pd.read_csv(inpt2)

df = pd.DataFrame((df_A.values + df_B.values)/2, columns = df_A.columns)
df['PMC'] = df['PMC'].astype(int)

df.to_csv(inpt3)

