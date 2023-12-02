# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:10:58 2023

@author: salva
"""

import csv
import os

def make_csv_files_same_size():
    # Get a list of all CSV files in the current directory
    csv_files = [file for file in os.listdir() if file.endswith(".csv")]

    # Determine the maximum number of columns among all CSV files
    max_columns = 0
    for csv_file in csv_files:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            max_columns = max(max_columns, len(next(reader, [])))

    # Update each CSV file to have the same number of columns
    for csv_file in csv_files:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Fill missing columns with spaces
        for row in data:
            row.extend([0] * (max_columns - len(row)))

        # Write the updated data back to the CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

if __name__ == "__main__":
    make_csv_files_same_size()