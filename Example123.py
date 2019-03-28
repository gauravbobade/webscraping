import sys
from importlib import reload
reload(sys)
#sys.setdefaultencoding('utf8')
# above code is commented because Since the default on Python 3 is UTF-8 already, there is no point in leaving those statements in.
# In Python 2, using sys.setdefaultencoding() was used to plaster over implicit encoding problems (caused by concatening byte strings and 
# unicode values, and other such mixed type situations), rather than fixing the problems themselves. Python 3 did away with implicit encoding 
# and decoding, so using the plaster to set a different encoding would make no difference anyway.

import csv
import requests
from bs4 import BeautifulSoup
url = 'http://www.espn.com/college-football/bcs/_/year/2013'
response = requests.get(url)
html = response.content

soup = BeautifulSoup((html), "lxml")
table = soup.find('table', attrs={'class': 'tablehead'})

list_of_rows = []
for row in table.findAll('tr')[0:]:
	list_of_cells=[]
	for cell in row.findAll('td'):
		text = cell.text.replace('&nbsp;','')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)

outfile = open ("D:\\Fall17\\Data Visualization\\Assignments\\Assignment2\\WebScraping_2019\\ranking.csv","w")
# In above code changed "wb" to "w" for Python 3. Because in Python 3 csv takes the input in text mode, whereas in Python 2 it took it in binary mode.

writer = csv.writer(outfile)
writer.writerows(list_of_rows)
