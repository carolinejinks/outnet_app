import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import wikipedia

html = urlopen("https://www.theoutnet.com/en-US/Shop/Designers")
bsObj = BeautifulSoup(html, "html.parser")

designer = []

for link in bsObj.find("div", {"class":"grid-12"}).findAll("a"):
    if 'data-urlkey' in link.attrs:
        designer.append(link.attrs['data-urlkey'])

summaries=[]
for n in designer:
    try:
        sum = wikipedia.summary(n)
        summaries.append(sum)
        print(summaries)
    except wikipedia.exceptions.PageError:
        continue
    except wikipedia.exceptions.DisambiguationError:
        continue
# you have list of all urllist

# function:
# open url, get the json/dict, then take out the value associated with extract (the key) - key:value pair
