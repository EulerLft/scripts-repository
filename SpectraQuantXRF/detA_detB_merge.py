# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:18:49 2023

@author: salva
"""

import pandas as pd 

inpt_1 = input('please input detA data: ')
inpt_2 = input('please input detB data: ')
inpt_3 = input('please input desired output file name: ')

df_detA = pd.read_csv(inpt_1)
df_detB = pd.read_csv(inpt_2)

df = df_detA + df_detB
df.to_csv(inpt_3)