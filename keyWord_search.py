# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:55:50 2023

@author: salva
"""

import os

def list_file_name(path):                                                      # list file names
    fileList = os.listdir(path)
    return(fileList)

def search_txt(path, keyWord):
    lsfiles = []
    for file in list_file_name(path):
        if file.endswith('.msa'):
            with open(path + '/' + file, 'r') as f:
                openFile = f.read()
                if keyWord in openFile:
                    lsfiles.append(file)
    lst = []
    if len(lsfiles)==0:
        return('No key word found ')
    else:
        return(lsfiles)
        lst.append(lsfiles)
    return(lst)
    