from bs4 import BeautifulSoup
import requests

import re
import json

file_name = '01x06'
season = 1
episode = 6
title = 'Jack Meets Dennis'

html_text = requests.get('https://transcripts.foreverdreaming.org/viewtopic.php?f=1083&t=46644').text
soup = BeautifulSoup(html_text, 'lxml')

chunks = soup.find('div', attrs={'class': 'postbody'})

lines = str(chunks.find_all('p'))
lines = re.sub('<p>', '', lines)
lines = re.sub('<br/>', '', lines)
lines = re.sub('\n', ' ', lines)
arr = lines.split('</p>, ')
 
clean = []
for line in arr:
    clean.append({"name": "", "line": f"{line.strip()}"})


dict = {
    "season":  season, 
    "episode": episode,
    "title": title,
    "script": clean
    
}
   
json_string = json.dumps(dict, indent=2)
json_string = re.sub('\"\[', '"', json_string)
json_string = re.sub('\]\"', '"', json_string)
json_string = re.sub('', '', json_string)

with open(f'episodes/30_rock_{file_name}.json', 'w') as data:
    data.write(json_string)

