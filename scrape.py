from bs4 import BeautifulSoup
import requests

import re
import json
import csv

episode = '01x04'

html_text = requests.get('https://transcripts.foreverdreaming.org/viewtopic.php?f=1083&t=46642').text
soup = BeautifulSoup(html_text, 'lxml')

chunks = soup.find('div', attrs={'class': 'postbody'})

lines = str(chunks.find_all('p'))

lines = re.sub('</*p>', '', lines)
lines = re.sub('<br/>', '', lines)


print(lines)
#for chunk in chunks:
#    
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
#   lines.append(clean)
#    
#print(lines)   
    
with open(f'{episode}.json', 'w') as data:
    json.dump(lines, data, ensure_ascii=False, indent=4)


#with open("output.csv", 'w', newline= '') as output:
##    wr = csv.writer(output, delimiter='/')
#    for element in lines:
#        wr.writerow([str(element)])
#    output.close()
#with open(f'{episode}.csv', 'w', newline="") as file:
#    mywriter = csv.writer(file, delimiter='/')
#    mywriter.writerows([lines])