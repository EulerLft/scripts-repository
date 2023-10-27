# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:31:02 2023

@author: salva
"""
import csv
import re
import os 
from keyWord_search import list_file_name as list_file_name
from keyWord_search import search_txt
from test3_0 import copy_content_between_lines


current_directory = os.getcwd()

txt_files_w_word = [file for file in os.listdir(current_directory) if file.endswith(".txt") and "log" in file]

lst = []
for file in txt_files_w_word:
    lst.append(file)

for item in lst:
    token = item[:8]
    input_file = item
    output_file = token + 'temporary.txt'
    
    start_line_number = 53
    end_line_number = 68
    
    copy_content_between_lines(input_file, output_file, start_line_number, end_line_number)


current_directory = os.getcwd()

txt_files_w_word = [file for file in os.listdir(current_directory) if file.endswith(".txt") and "temporary" in file]

lst = []
for file in txt_files_w_word:
    lst.append(file)

for item in lst: 
    token = item[:8]
    input_txt_file = item
    output_csv_file = token + '.csv'
    
    with open(input_txt_file, 'r') as txt_file, open(output_csv_file, 'w', newline="") as csv_file:
        # create CSV writer
        csv_writer = csv.writer(csv_file)
        
        for line in txt_file:
            # split the line using one or more spaces as the delimiter 
            columns = re.split(r'\s+', line.strip())
            
            # Write the columns to the CSV file
            csv_writer.writerow(columns)
            

[os.remove(file) for file in os.listdir() if file.endswith(".txt") and "temporary" in file]
        