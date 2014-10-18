from bs4 import BeautifulSoup
import urllib.request
import re
import sys

import urllib.request

f = sys.argv[1]

#inputfile = open('delawareLinks.txt')
outputfile = open('foo3.txt', 'w')
with urllib.request.urlopen(f) as url:
    s = url.read()
soup = BeautifulSoup(s)
    
w = 0
for a in soup.find_all("span"):  
    if(w == 14):
        outputfile.write(a.text)
        outputfile.write('\n')
        break    
    w = w + 1



outputfile.close()
#inputfile.close()
#table = soup("tr", {'class' : 'index_table_in' })
#print table
