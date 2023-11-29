# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:01:10 2023

@author: salva
"""

import matplotlib.pyplot as plt 
import pandas as pd 
from numpy import trapz

# Input file names (input & output files)
input_file = input('please input the file name you want to analyze: ')
output_file = input('please input a name for the output file: ')
input_PMC_file = input('please input the PMC file name associated: ')

# Load input file to DataFrame
df = pd.read_csv(input_file)
df = df.iloc[:,2:]

df_PMC = pd.read_csv(input_PMC_file)

lst_PMC = df_PMC['PMC'].tolist()

# peak ranges 
peakRanges = [152,172,174,202,205,244,247,272,278,314,319,397,402,
               440,442,493,546,601,665,716,725,774,781,851,926,979]


# Create DataFrames, channel lists and max list
element_names = ["Mg", "Al", "Si", "P", "S", "Rh", "K", "Ca", "Ti", "Cr", "Mn", "Fe", "Ni"]
dfs = {}
max_dfs = {}
channels = {}
# Fill dfs and channels
for i in range(len(element_names)):
    start = peakRanges[2 * i]
    end = peakRanges[2 * i + 1]
    dfs["df" + element_names[i]] = df.iloc[:, start:end]
    channels[element_names[i] + "_channels"] = list(range(start, end))

# Fill max_dfs 
for element in element_names:
    max_dfs[f"max_{element}"] = dfs[f"df{element}"].idxmax(axis=1)


# Background
backRanges = [150,152,172,174,202,205,244,247,272,278,314,
                319,397,402,440,442,493,496,537,545,601,609,
                652,665,716,725,774,781,851,863,918,926,979,987]


# Define the element names and their corresponding background channel ranges
element_back_ranges = {
    "NaMg": backRanges[0:2],
    "MgAl": backRanges[2:4],
    "AlSi": backRanges[4:6],
    "SiP": backRanges[6:8],
    "PS": backRanges[8:10],
    "SRh": backRanges[10:12],
    "RhK": backRanges[12:14],
    "KCaa": backRanges[14:16],
    "CaaCab": backRanges[16:18],
    "CabTi": backRanges[18:20],
    "TiaTib": backRanges[20:22],
    "TibCr": backRanges[22:24],
    "CrMn": backRanges[24:26],
    "MnFea": backRanges[26:28],
    "FeaFeb": backRanges[28:30],
    "FebNi": backRanges[30:32],
    "Niback": backRanges[32:34]
}

# Create DataFrames and get their lengths
len_back = {}
dfs_back = {}
for element, back_range in element_back_ranges.items():
    dfs_back[element] = df.iloc[:, back_range[0]:back_range[1]]
    len_back[element] = len(dfs_back[element].axes[1])

# Unload these from the main dfs & dfs_back DataFrames
dfMg = dfs["dfMg"]
dfAl = dfs["dfAl"]
dfSi = dfs["dfSi"]
dfP = dfs["dfP"]
dfS = dfs["dfS"]
dfRh = dfs["dfRh"]
dfK = dfs["dfK"]
dfCaa = dfs["dfCa"]
dfTia = dfs["dfTi"]
dfCr = dfs["dfCr"]
dfMn = dfs["dfMn"]
dfFea = dfs["dfFe"]
dfNi = dfs["dfNi"]

dfNaMg = dfs_back['NaMg']
dfMgAl = dfs_back['MgAl']
dfAlSi = dfs_back['AlSi']
dfSiP = dfs_back['SiP']
dfPS = dfs_back['PS']
dfSRh = dfs_back['SRh']
dfRhK = dfs_back['RhK']
dfKCaa = dfs_back['KCaa']
dfCaaCab = dfs_back['CaaCab']
dfCabTi = dfs_back['CabTi']
dfTiaTib = dfs_back['TiaTib']
dfTibCr = dfs_back['TibCr']
dfCrMn = dfs_back['CrMn']
dfMnFea = dfs_back['MnFea']
dfFeaFeb = dfs_back['FeaFeb']
dfFebNi = dfs_back['FebNi']
dfNiback = dfs_back['Niback']

# Name all background dataFrames
dataframes = [dfNaMg, dfMgAl, dfAlSi, dfSiP, dfPS, dfSRh, dfRhK, dfKCaa, dfCaaCab, 
              dfCabTi, dfTiaTib, dfTibCr, dfCrMn, dfMnFea, dfFeaFeb, dfFebNi, dfNiback]

# Avg Background
for df in dataframes:
    df['Mean Background'] = df.mean(axis=1)

# Max Channel 
data = {
    'Max Mg Channel': max_dfs['max_Mg'],
    'Max Al Channel': max_dfs['max_Al'],
    'Max Si Channel': max_dfs['max_Si'],
    'Max P Channel': max_dfs['max_P'],
    'Max S Channel': max_dfs['max_S'],
    'Max Rh Channel': max_dfs['max_Rh'],
    'Max K Channel': max_dfs['max_K'],
    'Max Ca(a) Channel': max_dfs['max_Ca'],
    'Max Ti(a) Channel': max_dfs['max_Ti'],
    'Max Cr Channel': max_dfs['max_Cr'],
    'Max Mn Channel': max_dfs['max_Mn'],
    'Max Fe(a) Channel': max_dfs['max_Fe'],
    'Max Ni Channel': max_dfs['max_Ni']
}

df1 = pd.DataFrame(data)
#df1.to_csv('analysisM1_maxChannel.csv')


# Define the column names you want to process
columns_to_process = [
    'NaMg', 'MgAl', 'AlSi', 'SiP', 'PS', 'SRh', 'RhK', 'KCaa',
    'CaaCab', 'CabTi', 'TiaTib', 'TibCr', 'CrMn', 'MnFea',
    'FeaFeb', 'FebNi', 'Niback'
]

# Create an empty dictionary to store the background lists
background_lists = {}

# Iterate through the columns and create background lists
for col in columns_to_process:
    df_col = globals()[f'df{col}']
    background_list = f'{col} avg. Back'
    background_lists[background_list] = [df_col.iloc[q, -1] for q in range(dfMg.shape[0])]

# Create a DataFrame from the dictionary
df_analysis = pd.DataFrame(background_lists)

# Save the DataFrame to a CSV file
#df_analysis.to_csv('analysisM1_back.csv')

#Analysis Script
# Peak Area
lstMg_peakArea = []
lstMg_peakAreaCorr = []
lstAl_peakArea = []
lstAl_peakAreaCorr = []
lstSi_peakArea = []
lstSi_peakAreaCorr = []
lstP_peakArea = []
lstP_peakAreaCorr = []
lstS_peakArea = []
lstS_peakAreaCorr = []
lstRh_peakArea = []
lstRh_peakAreaCorr = []
lstK_peakArea = []
lstK_peakAreaCorr = []
lstCaa_peakArea = []
lstCaa_peakAreaCorr = []
lstTia_peakArea = []
lstTia_peakAreaCorr = []
lstCr_peakArea = []
lstCr_peakAreaCorr = []
lstMn_peakArea = []
lstMn_peakAreaCorr = []
lstFea_peakArea = []
lstFea_peakAreaCorr = []
lstNi_peakArea = []
lstNi_peakAreaCorr = []

# Background

lstMg_areaBackground = []
lstAl_areaBackground = []
lstSi_areaBackground = []
lstP_areaBackground = []
lstS_areaBackground = []
lstRh_areaBackground = []
lstK_areaBackground = []
lstCaa_areaBackground = []
lstTia_areaBackground = []
lstCr_areaBackground = []
lstMn_areaBackground = []
lstFea_areaBackground = []
lstNi_areaBackground = []


for q in range(dfMg.shape[0]): 
    # Peak Area 
    tdf_Mg = pd.Series(dfMg.iloc[q,:])
    tdf_Mg = tdf_Mg.to_frame()
    tdf_Mg.columns = ['Count']
    tdf_Mg = tdf_Mg.reset_index(drop=True)
    y_Mg = tdf_Mg['Count']
    x_Mg = list(range(0,len(tdf_Mg.index)))
    area_Mg = trapz(y_Mg,x_Mg)
    lstMg_peakArea.append(area_Mg)
    
    tdf_Al = pd.Series(dfAl.iloc[q,:])
    tdf_Al = tdf_Al.to_frame()
    tdf_Al.columns = ['Count']
    tdf_Al = tdf_Al.reset_index(drop=True)
    y_Al = tdf_Al['Count']
    x_Al = list(range(0,len(tdf_Al.index)))
    area_Al = trapz(y_Al,x_Al)   
    lstAl_peakArea.append(area_Al)
    
    tdf_Si = pd.Series(dfSi.iloc[q,:])
    tdf_Si = tdf_Si.to_frame()
    tdf_Si.columns = ['Count']
    tdf_Si = tdf_Si.reset_index(drop=True)
    y_Si = tdf_Si['Count']
    x_Si = list(range(0,len(tdf_Si.index)))
    area_Si = (trapz(y_Si,x_Si))*1.1   
    lstSi_peakArea.append(area_Si)
    
    tdf_P = pd.Series(dfP.iloc[q,:])
    tdf_P = tdf_P.to_frame()
    tdf_P.columns = ['Count']
    tdf_P = tdf_P.reset_index(drop=True)
    y_P = tdf_P['Count']
    x_P = list(range(0,len(tdf_P.index)))
    area_P = (trapz(y_P,x_P))*1.1   
    lstP_peakArea.append(area_P)

    tdf_S = pd.Series(dfS.iloc[q,:])
    tdf_S = tdf_S.to_frame()
    tdf_S.columns = ['Count']
    tdf_S = tdf_S.reset_index(drop=True)
    y_S = tdf_S['Count']
    x_S = list(range(0,len(tdf_S.index)))
    area_S = (trapz(y_S,x_S))*1.1   
    lstS_peakArea.append(area_S)
    
    tdf_Rh = pd.Series(dfRh.iloc[q,:])
    tdf_Rh = tdf_Rh.to_frame()
    tdf_Rh.columns = ['Count']
    tdf_Rh = tdf_Rh.reset_index(drop=True)
    y_Rh = tdf_Rh['Count']
    x_Rh = list(range(0,len(tdf_Rh.index)))
    area_Rh = trapz(y_Rh,x_Rh)  
    lstRh_peakArea.append(area_Rh)
    
    tdf_K = pd.Series(dfK.iloc[q,:])
    tdf_K = tdf_K.to_frame()
    tdf_K.columns = ['Count']
    tdf_K = tdf_K.reset_index(drop=True)
    y_K = tdf_K['Count']
    x_K = list(range(0,len(tdf_K.index)))
    area_K = (trapz(y_K,x_K))*1.1   
    lstK_peakArea.append(area_K)
 
    tdf_Caa = pd.Series(dfCaa.iloc[q,:])
    tdf_Caa = tdf_Caa.to_frame()
    tdf_Caa.columns = ['Count']
    tdf_Caa = tdf_Caa.reset_index(drop=True)
    y_Caa = tdf_Caa['Count']
    x_Caa = list(range(0,len(tdf_Caa.index)))
    area_Caa = (trapz(y_Caa,x_Caa))*1.1   
    lstCaa_peakArea.append(area_Caa)    
    
    tdf_Tia = pd.Series(dfTia.iloc[q,:])
    tdf_Tia = tdf_Tia.to_frame()
    tdf_Tia.columns = ['Count']
    tdf_Tia = tdf_Tia.reset_index(drop=True)
    y_Tia = tdf_Tia['Count']
    x_Tia = list(range(0,len(tdf_Tia.index)))
    area_Tia = (trapz(y_Tia,x_Tia))*1.1   
    lstTia_peakArea.append(area_Tia)

    tdf_Cr = pd.Series(dfCr.iloc[q,:])
    tdf_Cr = tdf_Cr.to_frame()
    tdf_Cr.columns = ['Count']
    tdf_Cr = tdf_Cr.reset_index(drop=True)
    y_Cr = tdf_Cr['Count']
    x_Cr = list(range(0,len(tdf_Cr.index)))
    area_Cr = (trapz(y_Cr,x_Cr))*1.1   
    lstCr_peakArea.append(area_Cr)

    tdf_Mn = pd.Series(dfMn.iloc[q,:])
    tdf_Mn = tdf_Mn.to_frame()
    tdf_Mn.columns = ['Count']
    tdf_Mn = tdf_Mn.reset_index(drop=True)
    y_Mn = tdf_Mn['Count']
    x_Mn = list(range(0,len(tdf_Mn.index)))
    area_Mn = trapz(y_Mn,x_Mn)  
    lstMn_peakArea.append(area_Mn)
    
    tdf_Fea = pd.Series(dfFea.iloc[q,:])
    tdf_Fea = tdf_Fea.to_frame()
    tdf_Fea.columns = ['Count']
    tdf_Fea = tdf_Fea.reset_index(drop=True)
    y_Fea = tdf_Fea['Count']
    x_Fea = list(range(0,len(tdf_Fea.index)))
    area_Fea = (trapz(y_Fea,x_Fea))*1.1   
    lstFea_peakArea.append(area_Fea)

    tdf_Ni = pd.Series(dfNi.iloc[q,:])
    tdf_Ni = tdf_Ni.to_frame()
    tdf_Ni.columns = ['Count']
    tdf_Ni = tdf_Ni.reset_index(drop=True)
    y_Ni = tdf_Ni['Count']
    x_Ni = list(range(0,len(tdf_Ni.index)))
    area_Ni = trapz(y_Ni,x_Ni)   
    lstNi_peakArea.append(area_Ni)

    # Background 
    
    #Magnesium
    y1_Mg = df_analysis.iloc[q,0]
    y2_Mg = df_analysis.iloc[q,1]
    m_Mg = (y2_Mg - y1_Mg)/(173-151)
    x_values = list(range(0,(172-152)))  
    y_values = []    
    for x in x_values:
        y_temp = m_Mg*x + y1_Mg
        y_values.append(y_temp)
    
    Mg_areaBackground = trapz(y_values, x_values)
    lstMg_areaBackground.append(Mg_areaBackground)
    
    if Mg_areaBackground > area_Mg:
        Mg_areaCorr = area_Mg * 0.5
    else:
        Mg_areaCorr = area_Mg 

    lstMg_peakAreaCorr.append(Mg_areaCorr)
    
    
    #Aluminum
    y1_Al = df_analysis.iloc[q,1]
    y2_Al = df_analysis.iloc[q,2]
    m_Al = (y2_Al - y1_Al)/(204-173)
    x_values = list(range(0,(202-174)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_Al*x + y1_Al 
        y_values.append(y_temp)
    
    Al_areaBackground = trapz(y_values, x_values)
    lstAl_areaBackground.append(Al_areaBackground)
    
    if Al_areaBackground > area_Al:
        Al_areaCorr = area_Al * 0.5
    else:
        Al_areaCorr = area_Al
    
    lstAl_peakAreaCorr.append(Al_areaCorr)
    
    
    #Silicon
    y1_Si = df_analysis.iloc[q,2]
    y2_Si = df_analysis.iloc[q,3]
    m_Si = (y2_Si - y1_Si)/(245-204)
    x_values = list(range(0,(244-205)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_Si*x + y1_Si
        y_values.append(y_temp)
    
    Si_areaBackground = trapz(y_values, x_values)
    lstSi_areaBackground.append(Si_areaBackground)
    
    if Si_areaBackground > area_Si:
        Si_areaCorr = area_Si * 0.5
    else:
        Si_areaCorr = area_Si - Si_areaBackground
    
    lstSi_peakAreaCorr.append(Si_areaCorr)
    
    
    #Phosphorus
    y1_P = df_analysis.iloc[q,3]
    y2_P = df_analysis.iloc[q,4]
    m_P = (y2_P - y1_P)/(276-245)
    x_values = list(range(0,(272-247)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_P*x + y1_P
        y_values.append(y_temp)
    
    P_areaBackground = trapz(y_values, x_values)
    lstP_areaBackground.append(P_areaBackground)
    
    if P_areaBackground > area_P:
        P_areaCorr = area_P * 0.5
    else:
        P_areaCorr = area_P - P_areaBackground
    
    lstP_peakAreaCorr.append(P_areaCorr)
    
    
    #Sulfur
    y1_S = df_analysis.iloc[q,4]
    y2_S = df_analysis.iloc[q,5]
    m_S = (y2_S - y1_S)/(316-276)
    x_values = list(range(0,(314-278)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_S*x + y1_S
        y_values.append(y_temp)
    
    S_areaBackground = trapz(y_values, x_values)
    lstS_areaBackground.append(S_areaBackground)
    
    if S_areaBackground > area_S:
        S_areaCorr = area_S * 0.5
    else:
        S_areaCorr = area_S - S_areaBackground
    
    lstS_peakAreaCorr.append(S_areaCorr)

    #Rhodium
    y1_Rh = df_analysis.iloc[q,5]
    y2_Rh = df_analysis.iloc[q,6]
    m_Rh = (y2_Rh - y1_Rh)/(399-316)
    x_values = list(range(0,(397-319)))

    y_values = []    
    for x in x_values:
        y_temp = m_Rh*x + y1_Rh
        y_values.append(y_temp)
    
    Rh_areaBackground = trapz(y_values, x_values)
    lstRh_areaBackground.append(Rh_areaBackground)
    
    if Rh_areaBackground > area_Rh:
        Rh_areaCorr = area_Rh * 0.5
    else:
        Rh_areaCorr = area_Rh - Rh_areaBackground
    
    lstRh_peakAreaCorr.append(Rh_areaCorr)
    
    #Potassium
    y1_K = df_analysis.iloc[q,6]
    y2_K = df_analysis.iloc[q,7]
    m_K = (y2_K - y1_K)/(441-399)
    x_values = list(range(0,(440-402)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_K*x + y1_K
        y_values.append(y_temp)
    
    K_areaBackground = trapz(y_values, x_values)
    lstK_areaBackground.append(K_areaBackground)
    
    if K_areaBackground > area_K:
        K_areaCorr = area_K * 0.5
    else:
        K_areaCorr = area_K - K_areaBackground
    
    lstK_peakAreaCorr.append(K_areaCorr)
    
    #Calcium
    y1_Caa = df_analysis.iloc[q,7]
    y2_Caa = df_analysis.iloc[q,8]
    m_Caa = (y2_Caa - y1_Caa)/(494-441)
    x_values = list(range(0,(493-442)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_Caa*x + y1_Caa
        y_values.append(y_temp)
    
    Caa_areaBackground = trapz(y_values, x_values)
    lstCaa_areaBackground.append(Caa_areaBackground)
    
    if Caa_areaBackground > area_Caa:
        Caa_areaCorr = area_Caa * 0.5
    else:
        Caa_areaCorr = area_Caa - Caa_areaBackground
    
    lstCaa_peakAreaCorr.append(Caa_areaCorr)
    
    #Titanium
    y1_Tia = df_analysis.iloc[q,9]
    y2_Tia = df_analysis.iloc[q,10]
    m_Tia = (y2_Tia - y1_Tia)/(605-541)
    x_values = list(range(0,(601-546)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_Tia*x + y1_Tia
        y_values.append(y_temp)    
    
    Tia_areaBackground = trapz(y_values, x_values)
    lstTia_areaBackground.append(Tia_areaBackground)
    
    if Tia_areaBackground > area_Tia:
        Tia_areaCorr = area_Tia * 0.5
    else:
        Tia_areaCorr = area_Tia - Tia_areaBackground
    
    lstTia_peakAreaCorr.append(Tia_areaCorr)
    
    #Chromium
    y1_Cr = df_analysis.iloc[q,11]
    y2_Cr = df_analysis.iloc[q,12]
    m_Cr = (y2_Cr - y1_Cr)/(720-659)
    x_values = list(range(0,(716-665)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_Cr*x + y1_Cr
        y_values.append(y_temp)
    
    Cr_areaBackground = trapz(y_values, x_values)
    lstCr_areaBackground.append(Cr_areaBackground)
    
    if Cr_areaBackground > area_Cr:
        Cr_areaCorr = area_Cr * 0.5
    else:
        Cr_areaCorr = area_Cr - Cr_areaBackground
    
    lstCr_peakAreaCorr.append(Cr_areaCorr)

    #Manganese
    y1_Mn = df_analysis.iloc[q,12]
    y2_Mn = df_analysis.iloc[q,13]
    m_Mn = (y2_Mn - y1_Mn)/(778-720)
    x_values = list(range(0,(774-725)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_Mn*x + y1_Mn
        y_values.append(y_temp)
    
    Mn_areaBackground = trapz(y_values, x_values)
    lstMn_areaBackground.append(Mn_areaBackground)
    
    if Mn_areaBackground > area_Mn:
        Mn_areaCorr = area_Mn * 0.5
    else:
        Mn_areaCorr = area_Mn - Mn_areaBackground
    
    lstMn_peakAreaCorr.append(Mn_areaCorr)
    
    #Iron
    y1_Fea = df_analysis.iloc[q,13]
    y2_Fea = df_analysis.iloc[q,14]
    m_Fea = (y2_Fea - y1_Fea)/(858-778)
    x_values = list(range(0,(851-781)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_Fea*x + y1_Fea
        y_values.append(y_temp)
    
    Fea_areaBackground = trapz(y_values, x_values)
    lstFea_areaBackground.append(Fea_areaBackground)
    
    if Fea_areaBackground > area_Fea:
        Fea_areaCorr = area_Fea * 0.5
    else:
        Fea_areaCorr = area_Fea
        
    lstFea_peakAreaCorr.append(Fea_areaCorr)

    #Nickel
    y1_Ni = df_analysis.iloc[q,15]
    y2_Ni = df_analysis.iloc[q,16]
    m_Ni = (y2_Ni - y1_Ni)/(983-923)
    x_values = list(range(0,(979-926)))
    
    y_values = []    
    for x in x_values:
        y_temp = m_Ni*x + y1_Ni
        y_values.append(y_temp)
    
    Ni_areaBackground = trapz(y_values, x_values)
    lstNi_areaBackground.append(Ni_areaBackground)
    
    if Ni_areaBackground > area_Ni:
        Ni_areaCorr = area_Ni * 0.5
    else:
        Ni_areaCorr = area_Ni - Ni_areaBackground
        
    lstNi_peakAreaCorr.append(Ni_areaCorr)

dict = {'PMC':lst_PMC, 
       'Mg peak area M1':lstMg_peakAreaCorr,
       'Al peak area M1':lstAl_peakAreaCorr,
       'Si peak area M1':lstSi_peakAreaCorr,    
       'P peak area M1':lstP_peakAreaCorr,      
       'S peak area M1':lstS_peakAreaCorr,     
       'Rh peak area M1':lstRh_peakAreaCorr,      
       'K peak area M1':lstK_peakAreaCorr,
       'Ca peak area M1':lstCaa_peakAreaCorr,
       'Ti peak area M1':lstTia_peakAreaCorr,       
       'Cr peak area M1':lstCr_peakAreaCorr,       
       'Mn peak area M1':lstMn_peakAreaCorr,      
       'Fe peak area M1':lstFea_peakAreaCorr,       
       'Ni peak area M1':lstNi_peakAreaCorr}

df_final = pd.DataFrame(dict)
df_final.to_csv(output_file)
