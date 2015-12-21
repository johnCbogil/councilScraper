import csv
import requests
import re
import bs4

from BeautifulSoup import BeautifulSoup

url = 'http://council.nyc.gov/d51/html/members/home.shtml'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

tdNavText = soup.find('td', attrs={'class' : 'nav_text'})
text = tdNavText.text.replace('&nbsp;', '')

def getLegislativePhone():
	legislativePhoneWithTitle = re.search("((Legislative Office Phone)+.{12})", text)
	legislativePhone = "".join(re.findall('\d+', legislativePhoneWithTitle.group(0)))
	print legislativePhone

def getDistrictPhone():
	districtPhoneWithTitle = re.search("((District Office Phone)+.{12})", text)
	districtPhone = "".join(re.findall('\d+', districtPhoneWithTitle.group(0)))
	print districtPhone

def getMailto():
	for a in tdNavText.findAll('a'):
		if 'mailto' in a['href']:
  			print a.get('href')[7:]

getMailto()
