import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

csvfile = open("outnet.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
# write the header row for CSV file
c.writerow(['designer', 'links'])

html = urlopen("https://www.theoutnet.com/en-US/Shop/Designers")
bsObj = BeautifulSoup(html, "html.parser")


designer = []
links = []

for link in bsObj.find("div", {"class":"grid-12"}).findAll("a"):
    if 'data-urlkey' in link.attrs:
        designer.append(link.attrs['data-urlkey'])

for link in bsObj.find("div", {"class":"grid-12"}).findAll("a"):
    if 'href' in link.attrs:
        links.append(link.attrs['href'])

c.writerow( [designer, links] )
n = 0
for design in designer:

    c.writerow( [designer[n], links[n]] )
    n = n + 1


csvfile.close()
