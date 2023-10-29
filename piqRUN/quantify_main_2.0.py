# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:45:39 2023

@author: salva
"""

from keyWord_search import list_file_name as list_file_name
from keyWord_search import search_txt

lst = search_txt(input('Please input folder path: '), input('Please input key word: '))

for item in lst:
    token1 = item[:8]
    token2 = item[-10:-4] 
    spectrum_file = item
    plot_file = token1 + '_' + token2 + '_plot.csv'
    log_file = token1 + '_' + token2 + '_log.txt'
    
    lines = ['./Piquant', 'quant', '"Config_PIXL_FM_SurfaceOps_Rev1_Jul2021.msa"',
             '"Calibration_PIXL_FM_SurfaceOps_5minECFs_Rev1_Jul2021.csv"', spectrum_file,
             '"Na_K Mg_K Al_K Si_K P_K S_K Cl_K K_K Ca_K Ti_K Cr_K Mn_K Fe_K Ni_K Zn_K Br_K Ar_I"', plot_file, log_file]
    
    with open('cmnd_line.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write(' ')
        f.write('\n')
        f.write('\n')
    
    print('')
    print('***************************************************************************************') 
    print('QUANT BASE SCRIPT CREATED (' + token1 + '_' + token2 +') REFERENCE: ' + plot_file + ', ' + log_file)
    print('***************************************************************************************') 
    print('')
