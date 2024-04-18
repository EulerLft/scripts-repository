# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:45:29 2023

@author: salva
"""

import pandas as pd
import numpy as np


# Chunks : Yield successive n-sized chunks from lst
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
### 1.
### Loop the data lines
with open(input('please enter RFS file name as a string: '), 'r') as temp_f:
    # get number of columns in each line
    col_count = [ len(l.split(",")) for l in temp_f.readlines() ]

### Generate column names  (names will be 0, 1, 2, ..., maximum columns - 1)
column_names = [i for i in range(0, max(col_count))]

inpt1 = input('Please input the rfs file you want to analyze: ')

### Read csv
df = pd.read_csv(inpt1, header=None, delimiter=",", names=column_names);


### 2.
### Assign the first row as headers and reset index
df.columns = df.iloc[0]
df = df[1:]
df.reset_index(drop=True, inplace=True)



### 3.  
### Obtain the index of the 'x' label of the PCM spreadsheet
x = int(df[df['SCLK_B']=='x'].index.values)
x

# SCLK 
df_SCLK = df.loc[0:x-1]
df_SCLK = df_SCLK.loc[:,:'OFFSET_B']

# PCM 
df_PCM = df.loc[x:x+x]
df_PCM.reset_index(drop=True, inplace=True)
new_header = df_PCM.iloc[0]
df_PCM = df_PCM[1:]
df_PCM.columns = new_header
df_PCM.reset_index(drop=True, inplace=True)
df_PCM = df_PCM.loc[:, :'z']

# Det A 
df_DetA = df.loc[x+x+1:x+x+x+1]
df_DetA.reset_index(drop=True, inplace=True)
new_headers = df_DetA.iloc[0]
df_DetA = df_DetA[1:]
df_DetA.columns = new_headers
df_DetA.reset_index(drop=True, inplace=True)

# Det B 
df_DetB = df.loc[x+x+x+2:x+x+x+x+3]
df_DetB.reset_index(drop=True, inplace=True)
new_header = df_DetB.iloc[0]
df_DetB = df_DetB[1:]
df_DetB.columns = new_header
df_DetB.reset_index(drop=True, inplace=True)
#df_DetB.drop(index=df_DetB.index[-1], axis=0, inplace=True)

# Save as .csv
df_SCLK.to_csv('SCLK.csv')
df_PCM.to_csv('PMC.csv')
df_DetA.to_csv('DetA.csv')
df_DetB.to_csv('DetB.csv')


# 1.)

## [NOTE: not sure why importing DetA from the .csv matters. My guess is that I need the additional headers for things
# to work out. Otherwise obtain NaN entries and mismatched lengths.] 

df_DetA_2 = pd.read_csv('DetA.csv')
df_livetime_A = pd.read_csv('SCLK.csv')
df_livetime_A = df_livetime_A['live_time_A']
df_livetime_A = df_livetime_A.to_frame()

data = []

for i in range(df_livetime_A.shape[0]):
    val = df_livetime_A.at[i, 'live_time_A']
    for i in range(len(df_DetA_2.columns)):
        data.append(val)

temp = list(chunks(data, 4097))
livetime_A = pd.DataFrame.from_records(temp)
livetime_A = livetime_A.reset_index(drop=True)

# 1.) b

df_DetB_2 = pd.read_csv('DetB.csv')
df_DetB_2 = df_DetB_2.iloc[:,1:]
df_livetime_B = pd.read_csv('SCLK.csv')
df_livetime_B = df_livetime_B['live_time_B']
df_livetime_B = df_livetime_B.to_frame()

# loop builds list 
data = []

for i in range(df_livetime_B.shape[0]):
    val = df_livetime_B.at[i, 'live_time_B']
    for i in range(len(df_DetB_2.columns)):
        data.append(val)

# create a list of data  // create a dataframe from list 'x'
temp = list(chunks(data, 4097))
livetime_B = pd.DataFrame.from_records(temp)
livetime_B = livetime_B.reset_index(drop=True)
livetime_B = livetime_B.iloc[:,1:]
#livetime_B = livetime_B[:-1]


lst = []
for i in list(range(0,len(df_livetime_B))):
    temp_Val = df_livetime_B.iloc[i,0]
    lst.append(temp_Val)

lstDetA = []

for i in list(range(0, len(lst))):
    value = lst[i]
    lstTemp = df_DetA.iloc[i, :].values.flatten().tolist()
    lstTemp = [int(x) for x in lstTemp]
    lstTemp = [x/value for x in lstTemp]
    lstDetA.append(lstTemp)
    
df_DetA2 = pd.DataFrame(lstDetA)
df_DetA2.to_csv('DetA_cps.csv')

lstDetB = []

for i in list(range(0, len(lst))):
    value = lst[i]
    lstTemp = df_DetB.iloc[i, :].values.flatten().tolist()
    lstTemp = [int(x) for x in lstTemp]
    lstTemp = [x/value for x in lstTemp]
    lstDetB.append(lstTemp)
    
df_DetB2 = pd.DataFrame(lstDetB)
df_DetB2.to_csv('DetB_cps.csv')

