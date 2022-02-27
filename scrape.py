from bs4 import BeautifulSoup
import requests

import re
import json

episode = '01x01'

html_text = requests.get('https://transcripts.foreverdreaming.org/viewtopic.php?f=1083&t=46639').text
soup = BeautifulSoup(html_text, 'lxml')

chunks = str(soup.find_all('div', attrs={'class': 'postbody'}))

lines = re.sub('</*p>', '', chunks)
lines = re.sub('<br/>', '', lines)
lines = re.sub('</*div>', '', lines)

#print(lines)
#for chunk in chunks:
##    
#    dirty_lines = chunk.find('p')
#    clean = []
#    for x in dirty_lines:
#        strencode = x.text.encode("ascii", "ignore")
#        temp= strencode.decode()
#        temp = re.sub('\s\s+', ' ', temp)
#        temp = temp.replace('.u00a0', '')
#        temp = temp.strip()
#        clean.append(re.sub('<.+>', '', temp))
#    clean = ' '.join(clean)
#    lines.append(clean)
    
#print(lines)   
    
with open(f'{episode}.json', 'w') as data:
    json.dump(lines, data, ensure_ascii=False, indent=4)