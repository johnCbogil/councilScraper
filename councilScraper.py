import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://council.nyc.gov/d17/html/members/home.shtml'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
td = soup.find('td')
table = soup.find('table')
tbody = soup.find('tbody')
print table
