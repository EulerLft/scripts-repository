# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:10:42 2024

@author: salva
"""

import pandas as pd 
import numpy as np

inpt1 = input('Please input the molar table file name (modified rqc/PIQUANT output file): ') 
inpt2 = input('Please input the oxide file name (rqc/PIQUANT output file): ')
inpt3 = input('Please input the PMC file name: ')
inpt4 = input('Please input the SCLK file name: ')

# Load the molar table & separate them into molar and ratio sub-tables 
df = pd.read_csv(inpt1)
df_molar = df.iloc[:, 2:-5]
df_ratio = df.iloc[:, -5:]

# Load and trim the oxides table; then find the sum oxides (last column in the product df_ox)
df_ox = pd.read_csv(inpt2)
df_ox = df_ox.iloc[:, 1:]
df_ox['Sum_ox%'] = df_ox.iloc[:, 0:16].sum(axis=1)

# Load the PMC tables
df_PMC = pd.read_csv(inpt3)
lst_PMC = df_PMC.iloc[:, 0]

# Load the SCLK tables and obtain the livetimes (livetimeA/B)
df_SCLK = pd.read_csv(inpt4)
df_SCLK = df_SCLK.iloc[:, [5,6]]

# Create a master df with all of the above (see below for order)
df_full = pd.concat([df_PMC, df_SCLK, df_ox, df_molar, df_ratio], axis=1)

total_ox = df_full['Sum_ox%']

# Obtain the oxide score (see notes for details)
olivine_oxide_score = (df_full['MgO_wt%'] + df_full['SiO2_wt%'] + df_full['FeO-T_wt%'])/total_ox
pyrxoene_oxide_score = (df_full['MgO_wt%'] + df_full['CaO_wt%'] + df_full['SiO2_wt%'] + df_full['FeO-T_wt%'])/total_ox
feldspar_oxide_score = (df_full['K2O_wt%'] + df_full['Na2O_wt%'] + df_full['Al2O3_wt%'] + df_full['SiO2_wt%'])/total_ox
silica_oxide_score = (df_full['SiO2_wt%'])/total_ox

# Insert the oxide scores into the table
df_full['olivine oxide score'] = olivine_oxide_score
df_full['pyroxene oxide score'] = pyrxoene_oxide_score
df_full['feldspar oxide score'] = feldspar_oxide_score
df_full['silica oxide score'] = silica_oxide_score

conditions = [
    ((df_full['(Mg+Fe+Ca)/Si'] >= 1.7) & (df_full['(Mg+Fe+Ca)/Si'] <= 2.3) & df_full['olivine oxide score'] >= 0.7) | (df_full['olivine oxide score'] >= 0.92),
    ((df_full['(Mg+Fe+Ca)/Si'] > 0.85) & (df_full['(Mg+Fe+Ca)/Si'] < 1.15)) | ((df_full['pyroxene oxide score'] >= 0.90) |
                                                                              (df_full['olivine oxide score'] >= 0.92) & (df_full['CaO_wt%'] >5)),
    ((df_full['olivine oxide score'] > 0.75) & (df_full['pyroxene oxide score'] > 0.75)),
    ((df_full['(K+Na+Al)/Si'] > 0.57) & (df_full['(K+Na+Al)/Si'] < 0.77)) | (df_full['feldspar oxide score'] > 0.8),
    (df_full['silica oxide score'] > 0.85)
]

values = ['OLIVINE', 'PYROXENE', 'OL/PYR MIX', 'FELDSPAR', 'PURE SILICA']

df_full['Mineral Identifier'] = np.select(conditions, values, default='UNKNOWN')



inpt5 = input('Please input the desired output file name:')

df_full.to_csv(inpt5)


