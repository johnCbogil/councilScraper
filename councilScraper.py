import csv
import requests
import re

from BeautifulSoup import BeautifulSoup

url = 'http://council.nyc.gov/d17/html/members/home.shtml'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
td = soup.find('td', attrs={'class' : 'nav_text'})

text = td.text.replace('&nbsp;', '')


phoneWithName = re.search("((Legislative Office Phone)+.{12})", text)

print phoneWithName.group(1)

string = "".join(re.findall('\d+', phoneWithName.group(1)))



print string