from pathlib import Path
import json
import os
import pandas as pd

directory = '/home/hamhams/Documents/GitHub/30-Rock/episodes'

column_names = ['season', 'episode', 'title', 'name', 'quote']

files = Path(directory).glob('*')
file_arr = []
json_arr = []
for root, dirs, files in os.walk(directory):
    for filename in files:
        file_arr.append(os.path.join(root, filename))
      
df = pd.DataFrame(columns=column_names)



for file in file_arr:
    with open(file) as f:
        data = json.load(f)
        
        for line in data['script']:
            temp = []
        
            for k, v in line.items():
                temp.append(v)   
            
            dict = [data['season'], data['episode'], data['title'], temp[0], temp[1]]
            
            df.loc[len(df)] = (dict)   
    
df.to_csv('all_scripts.csv')

