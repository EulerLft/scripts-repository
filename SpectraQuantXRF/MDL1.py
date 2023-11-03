L# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 16:42:41 2023

@author: salva
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import rc 

def intensity(x, mu_in, mu_out):
    return np.exp(-(mu_in + mu_out)*x)

rho_Fe = 7.874
rho_Si = 2.330 
rho_Ca = 1.55

mu_Fe_in = [736.3,557.6,55.56,305.6,25.68]
mu_Fe_in = [x*rho_Fe for x in mu_Fe_in]

mu_Si_in = [1318,978.4,94.88,64.69,4.46]
mu_Si_in = [x*rho_Si for x in mu_Si_in]

mu_Ca_in = [355.5,267.6,247.4,172.7,13.06]
mu_Ca_in = [x*rho_Ca for x in mu_Ca_in]

mu_Fe_out = 71.04*rho_Fe
mu_Si_out = 358.9*rho_Si
mu_Ca_out = 151.8*rho_Ca

x_lst = []
lst_Fe = []
lst_Si = []
lst_Ca = []

for x in list(range(0,len(mu_Fe_in))):
    muFe_in = mu_Fe_in[x]
    muSi_in = mu_Si_in[x]
    muCa_in = mu_Ca_in[x]
    tempLst_Fe = []
    tempLst_Si = []
    tempLst_Ca = []
    
    for i in list(np.linspace(0, 0.005, 100)):
        x_lst.append(i)
        temp_Fe = intensity(i, muFe_in, mu_Fe_out)
        if temp_Fe > 0.005:
            temp_Fe = temp_Fe
        else: 
            temp_Fe = 0
        tempLst_Fe.append(temp_Fe)
        
        temp_Si = intensity(i, muSi_in, mu_Si_out)
        if temp_Si > 0.005:
            temp_Si = temp_Si
        else:
            temp_Si = 0
        tempLst_Si.append(temp_Si)
    
        temp_Ca = intensity(i, muCa_in, mu_Si_out)
        if temp_Ca > 0.005:
            temp_Ca = temp_Ca
        else: 
            temp_Ca = 0
        tempLst_Ca.append(temp_Ca)
        
    lst_Fe.append(tempLst_Fe)
    lst_Si.append(tempLst_Si)
    lst_Ca.append(tempLst_Ca)
    
       
dict = {'x (depth) [cm]': x_lst[:100], r' $I/I_{0}$ [Fe 2.7keV]': lst_Fe[0], r' $I/I_{0}$ [Fe 3keV]': lst_Fe[1], 
        r' $I/I_{0}$ [Fe 7keV]': lst_Fe[2], r' $I/I_{0}$ [Fe 8keV]': lst_Fe[3], r' $I/I_{0}$ [Fe 20keV]': lst_Fe[4],
        r' $I/I_{0}$ [Si 2.7keV]': lst_Si[0], r' $I/I_{0}$ [Si 3keV]': lst_Si[1], r' $I/I_{0}$ [Si 7keV]': lst_Si[2], 
        r' $I/I_{0}$ [Si 8keV]': lst_Si[3], r' $I/I_{0}$ [Si 20keV]': lst_Si[4], r' $I/I_{0}$ [Ca 2.7keV]': lst_Ca[0],
       r' $I/I_{0}$ [Ca 3keV]':lst_Ca[1], r' $I/I_{0}$ [Ca 7keV]':lst_Ca[2], r' $I/I_{0}$ [Ca 8keV]':lst_Ca[3],
       r' $I/I_{0}$ [Ca 20keV]':lst_Ca[4]}
df_final = pd.DataFrame(dict)

df_final.to_csv('df_final(spyder).csv')