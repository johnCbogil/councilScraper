import csv
import requests
import re

from BeautifulSoup import BeautifulSoup

url = 'http://council.nyc.gov/d51/html/members/home.shtml'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
tdNavText = soup.find('td', attrs={'class' : 'nav_text'})


text = tdNavText.text.replace('&nbsp;', '')


def getEmail():
	tdNavText = soup.find('td', attrs={'class' : 'nav_text'})
	print tdNavText
	email = re.findall("\w+", tdNavText.text)
	print email

def getLegislativePhone():
	legislativePhoneWithTitle = re.search("((Legislative Office Phone)+.{12})", text)
	legislativePhone = "".join(re.findall('\d+', legislativePhoneWithTitle.group(0)))
	print legislativePhone

def getDistrictPhone():
	districtPhoneWithTitle = re.search("((District Office Phone)+.{12})", text)
	districtPhone = "".join(re.findall('\d+', districtPhoneWithTitle.group(0)))
	print districtPhone

getEmail()
