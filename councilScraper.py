import csv
import requests

from BeautifulSoup import BeautifulSoup

url = 'http://council.nyc.gov/d17/html/members/home.shtml'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
td = soup.find('td', attrs={'class' : 'nav_text'})

text = td.text.replace('&nbsp;', '')

print text
