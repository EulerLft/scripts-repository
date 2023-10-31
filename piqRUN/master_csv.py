# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:02:42 2023

@author: salva
"""

import os 
import pandas as pd 

inpt = input('please input the PMC file: ')
df_PMC = pd.read_csv(inpt)

csv_files = [file for file in os.listdir() if file.endswith('.csv') and 'log' in file]

# Initialize a dictionary to store DataFrames with names
dataframes = {}

# Iterate through each .csv file and read it into a DataFrame
for csv_file in csv_files:
    # Extract the DataFrame name from the last 4 characters of the file name
    token = csv_file[:8]
    df_name = csv_file[:-5]  # Remove the ".csv" extension
    dataframes[df_name] = pd.read_csv(csv_file, header=None)
        
name = token + '_master.csv'

lst_ox_Na = []
lst_ox_Mg = []
lst_ox_Al = []
lst_ox_Si = []
lst_ox_P = []
lst_ox_S = []
lst_ox_Cl = []
lst_ox_K = []
lst_ox_Ca = []
lst_ox_Ti = []
lst_ox_Cr = []
lst_ox_Mn = []
lst_ox_Fe = []
lst_ox_Ni = []
lst_ox_Zn = []
lst_ox_Br = []

lst_peak_Na = []
lst_peak_Mg = []
lst_peak_Al = []
lst_peak_Si = []
lst_peak_P = []
lst_peak_S = []
lst_peak_Cl = []
lst_peak_K = []
lst_peak_Ca = []
lst_peak_Ti = []
lst_peak_Cr = []
lst_peak_Mn = []
lst_peak_Fe = []
lst_peak_Ni = []
lst_peak_Zn = []
lst_peak_Br = []

lst_error_Na = []
lst_error_Mg = []
lst_error_Al = []
lst_error_Si = []
lst_error_P = []
lst_error_S = []
lst_error_Cl = []
lst_error_K = []
lst_error_Ca = []
lst_error_Ti = []
lst_error_Cr = []
lst_error_Mn = []
lst_error_Fe = []
lst_error_Ni = []
lst_error_Zn = []
lst_error_Br = []

lst_emblem = []

for item in dataframes:
    emblem = item[9:-4]
    lst_emblem.append(emblem)
    
    ox_Na = dataframes[item].iloc[0,1]
    ox_Mg = dataframes[item].iloc[1,1]
    ox_Al = dataframes[item].iloc[2,1]
    ox_Si = dataframes[item].iloc[3,1]
    ox_P = dataframes[item].iloc[4,1]
    ox_S = dataframes[item].iloc[5,1]
    ox_Cl = dataframes[item].iloc[6,1]
    ox_K = dataframes[item].iloc[7,1]
    ox_Ca = dataframes[item].iloc[8,1]
    ox_Ti = dataframes[item].iloc[9,1]
    ox_Cr = dataframes[item].iloc[10,1]
    ox_Mn = dataframes[item].iloc[11,1]
    ox_Fe = dataframes[item].iloc[12,1]
    ox_Ni = dataframes[item].iloc[13,1]
    ox_Zn = dataframes[item].iloc[14,1]
    ox_Br = dataframes[item].iloc[15,1]
    
    peak_Na = dataframes[item].iloc[0,5]
    peak_Mg = dataframes[item].iloc[1,5]
    peak_Al = dataframes[item].iloc[2,5]
    peak_Si = dataframes[item].iloc[3,5]
    peak_P = dataframes[item].iloc[4,5]
    peak_S = dataframes[item].iloc[5,5]
    peak_Cl = dataframes[item].iloc[6,5]
    peak_K = dataframes[item].iloc[7,5]
    peak_Ca = dataframes[item].iloc[8,5]
    peak_Ti = dataframes[item].iloc[9,5]
    peak_Cr = dataframes[item].iloc[10,5]
    peak_Mn = dataframes[item].iloc[11,5]
    peak_Fe = dataframes[item].iloc[12,5]
    peak_Ni = dataframes[item].iloc[13,5]
    peak_Zn = dataframes[item].iloc[14,5]
    peak_Br = dataframes[item].iloc[15,5]
    
    error_Na = dataframes[item].iloc[0,11]
    error_Mg = dataframes[item].iloc[1,11]
    error_Al = dataframes[item].iloc[2,11]
    error_Si = dataframes[item].iloc[3,11]
    error_P = dataframes[item].iloc[4,11]
    error_S = dataframes[item].iloc[5,11]
    error_Cl = dataframes[item].iloc[6,11]
    error_K = dataframes[item].iloc[7,11]
    error_Ca = dataframes[item].iloc[8,11]
    error_Ti = dataframes[item].iloc[9,11]
    error_Cr = dataframes[item].iloc[10,11]
    error_Mn = dataframes[item].iloc[11,11]
    error_Fe = dataframes[item].iloc[12,11]
    error_Ni = dataframes[item].iloc[13,11]
    error_Zn = dataframes[item].iloc[14,11]
    error_Br = dataframes[item].iloc[15,11]
    
    lst_ox_Na.append(ox_Na)
    lst_ox_Mg.append(ox_Mg)
    lst_ox_Al.append(ox_Al)
    lst_ox_Si.append(ox_Si)
    lst_ox_P.append(ox_P)
    lst_ox_S.append(ox_S)
    lst_ox_Cl.append(ox_Cl)
    lst_ox_K.append(ox_K)
    lst_ox_Ca.append(ox_Ca)
    lst_ox_Ti.append(ox_Ti)
    lst_ox_Cr.append(ox_Cr)
    lst_ox_Mn.append(ox_Mn)
    lst_ox_Fe.append(ox_Fe)
    lst_ox_Ni.append(ox_Ni)
    lst_ox_Zn.append(ox_Zn)
    lst_ox_Br.append(ox_Br)
    
    lst_peak_Na.append(peak_Na)
    lst_peak_Mg.append(peak_Mg)
    lst_peak_Al.append(peak_Al)
    lst_peak_Si.append(peak_Si)
    lst_peak_P.append(peak_P)
    lst_peak_S.append(peak_S)
    lst_peak_Cl.append(peak_Cl)
    lst_peak_K.append(peak_K)
    lst_peak_Ca.append(peak_Ca)
    lst_peak_Ti.append(peak_Ti)
    lst_peak_Cr.append(peak_Cr)
    lst_peak_Mn.append(peak_Mn)
    lst_peak_Fe.append(peak_Fe)
    lst_peak_Ni.append(peak_Ni)
    lst_peak_Zn.append(peak_Zn)
    lst_peak_Br.append(peak_Br)
    
    lst_error_Na.append(error_Na)
    lst_error_Mg.append(error_Mg)
    lst_error_Al.append(error_Al)
    lst_error_Si.append(error_Si)
    lst_error_P.append(error_P)
    lst_error_S.append(error_S)
    lst_error_Cl.append(error_Cl)
    lst_error_K.append(error_K)
    lst_error_Ca.append(error_Ca)
    lst_error_Ti.append(error_Ti)
    lst_error_Cr.append(error_Cr)
    lst_error_Mn.append(error_Mn)
    lst_error_Fe.append(error_Fe)
    lst_error_Ni.append(error_Ni)
    lst_error_Zn.append(error_Zn)
    lst_error_Br.append(error_Br)
    
    
data = {
    'emblem':lst_emblem,
    'Na ox%':lst_ox_Na,
    'Na peak area':lst_peak_Na,
    'Na abs error':lst_error_Na,
    'Mg ox%':lst_ox_Mg,
    'Mg peak area':lst_peak_Mg,
    'Mg abs error':lst_error_Mg,
    'Al ox%':lst_ox_Al,
    'Al peak area':lst_peak_Al,
    'Al abs error':lst_error_Al,
    'Si ox%':lst_ox_Si,
    'Si peak area':lst_peak_Si,
    'Si abs error':lst_error_Si,
    'P ox%':lst_ox_P,
    'P peak area':lst_peak_P,
    'P abs error':lst_error_P,
    'S ox%':lst_ox_S,
    'S peak area':lst_peak_S,
    'S abs error':lst_error_S,
    'Cl ox%':lst_ox_Cl,
    'Cl peak area':lst_peak_Cl,
    'Cl abs error':lst_error_Cl,
    'K ox%':lst_ox_K,
    'K peak area':lst_peak_K,
    'K abs error':lst_error_K,
    'Ca ox%':lst_ox_Ca,
    'Ca peak area':lst_peak_Ca,
    'Ca error':lst_error_Ca,
    'Ti ox%':lst_ox_Ti,
    'Ti peak area':lst_peak_Ti,
    'Ti abs error':lst_error_Ti,
    'Cr ox%':lst_ox_Cr,
    'Cr peak area':lst_peak_Cr,
    'Cr abs error':lst_error_Cr,
    'Mn ox%':lst_ox_Mn,
    'Mn peak area':lst_peak_Mn,
    'Mn abs error':lst_error_Mn,
    'Fe ox%':lst_ox_Fe,
    'Fe peak area':lst_peak_Fe,
    'Fe abs error':lst_error_Fe,
    'Ni ox%':lst_ox_Ni,
    'Ni peak':lst_peak_Ni,
    'Ni abs error':lst_error_Ni,
    'Zn ox%':lst_ox_Zn,
    'Zn peak area%':lst_peak_Zn,
    'Zn abs error':lst_error_Zn,
    'Br ox%':lst_ox_Br,
    'Br peak area':lst_peak_Br,
    'Br abs error':lst_error_Br,
}


df = pd.DataFrame(data)
df['shot_number'] = df['emblem'].str.split('_').str[1].astype(int)
df = df.sort_values(by='shot_number')
df = df.drop(columns='shot_number')
df = df.reset_index(drop=True)

PMC = df_PMC.iloc[:,0].values

df.insert(0, 'PMC', PMC)
df = df.reset_index(drop=True)

df.to_csv(name)