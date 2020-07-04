#! /usr/bin/env python3

import os
import requests
import json

#define the path
path = "/data/feedback/"
#list files in the directory
dirs = os.listdir(path)
#define an empty directory
fields = ['title', 'name', 'date', 'feedback']
#travers through the files in the directory
#open the files
#go through the lines 
#strip by line
for file in dirs:
   dict1 = {}
   key_number = 0
   with open (path + file) as fh:
     for line in fh:
       description = line.strip() 
       dict1[fields[key_number]] = description
       key_number += 1
   print(dict1)
   response = requests.post(:http://35.232.128.93/feedback/",json=dict1)
print(response.request.bosy)
print(response.status_code) 
