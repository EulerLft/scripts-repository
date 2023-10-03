# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:59:37 2023

@author: salva
"""

import os 
import requests

def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)                                               # create folder if it doesn't already exist
    
    filename = url.split('/')[-1].replace(' ', '_')                            # be careful with file names
    file_path = os.path.join(dest_folder, filename)
    
    r = requests.get(url, stream=True)
    if r.ok:
        print('saving to', os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else: 
        print('Download failed: status code {}\n{}'.format(r.status_code, r.text))

