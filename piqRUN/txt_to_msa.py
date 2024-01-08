# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 18:02:14 2023

@author: salva
"""

import os
import pandas as pd 

inpt = input('please input the SCLK file name: ')

standards = pd.read_csv(inpt, header=0)
#standards = standards.iloc[:,1:]

realtime_A = []
realtime_B = []
livetime_A = []
livetime_B = []
yp_temp = []


for i in list(range(0, len(standards))):
    
    # Get the values we need from the SCLK.csv
    realtimeA = standards.iloc[i,3]
    realtimeB = standards.iloc[i,4]
    timeA = standards.iloc[i,5]
    timeB = standards.iloc[i,6]
    y_p_temp = standards.iloc[i,7]

    # Append values to lists
    realtime_A.append(realtimeA)
    realtime_B.append(realtimeB)
    livetime_A.append(timeA)
    livetime_B.append(timeB)
    yp_temp.append(y_p_temp)

lst = []


for i in list(range(0, len(realtime_A))):
    
    lines = ["#FORMAT      : EMSA/MAS spectral data file", 
             "#VERSION     : TC202v2.0 PIXL",
             "#TITLE       : N/A",
             "#DATE        :       Date in the format DD-MMM-YYYY, for example 07-JUL-2010",
             "#TIME        :             The time of day at which the spectrum was recorded, in 24-hour format",
             "#OWNER       : PIXL Flight Model       (PIXL will use this to indicate which instrument took the data.)",
             "#NPOINTS     : 4096     Number of data points in the spectrum (This can be zero for configuration only files)",
             "#NCOLUMNS    : 2     Number of data columns in the spectrum (This can be zero for configuration only files)",
             "#XUNITS      : eV",
             "#YUNITS      : COUNTS",
             "#DATATYPE    : YY",
             "#XPERCHAN    : 7.862, 7.881   eV per channel (separate by commas if more than one detector)",
             "#OFFSET      : 18.5, -22.4         eV of first channel  (separate by commas if more than one detector",
             "#SIGNALTYPE  : XRF",
             "#YP_TEMP     : " + str(yp_temp[i]),
             "#LIVETIME    : " + str(livetime_A[i]) + ", " + str(livetime_B[i]) + "   seconds (separate by commas if more than one detector)",
             "#REALTIME    : " + str(realtime_A[i]) + ", " + str(realtime_B[i]) + "   seconds (separate by commas if more than one detector)",
             "#SPECTRUM    : start of spectrum data"]    
    lst.append(lines)
    
# Get a list of all text files in the current directory
txt_files = [file for file in os.listdir() if file.endswith('.txt')]

# Define a function to extract the shot number from the file name
def extract_shot_number(filename):
    try:
        # Split the filename using underscores and extract the part containing the shot number
        shot_part = filename.split('_shot_')[1]
        # Remove the ".txt" extension and return the shot number as an integer
        return int(shot_part.split('.txt')[0])
    except (IndexError, ValueError):
        # Handle cases where the filename doesn't match the expected pattern
        return float('inf')  # Use infinity as a placeholder for sorting

# Sort the txt_files list based on the shot numbers
txt_files.sort(key=extract_shot_number)


for i, txt_file in enumerate(txt_files):
    # Read the content of the existing text file
    with open(txt_file, 'r') as txt_file_obj:
        existing_content = txt_file_obj.read()

    # Write the new lines followed by the existing content
    with open(txt_file, 'w') as txt_file_obj:
        txt_file_obj.write("\n".join(lst[i]) + "\n" + existing_content)


[os.rename(f, f.replace('.txt', '.msa')) for f in os.listdir() if f.endswith('.txt')]
[open(file, 'a').write('#ENDOFDATA     end of spectrum data\n') for file in os.listdir() if file.endswith('.msa')]

print('\n')
print(".msa files created")
