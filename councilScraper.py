import csv
import requests
import re
import bs4

from BeautifulSoup import BeautifulSoup

districtNumber = 1

while districtNumber <= 51:

	url = 'http://council.nyc.gov/d%d/html/members/home.shtml' % (districtNumber)
	print url
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)

	contactInfoHTML = soup.find('td', attrs={'class' : 'nav_text'})
	contactInfo = contactInfoHTML.text.replace('&nbsp;', '')

	def getLegislativePhone():
		legislativePhoneWithTitle = re.search("((Legislative Office Phone)+.{12})", contactInfo)
		legislativePhone = "".join(re.findall('\d+', legislativePhoneWithTitle.group(0)))
		print legislativePhone

	def getDistrictPhone():
		districtPhoneWithTitle = re.search("((District Office Phone)+.{12})", contactInfo)
		districtPhone = "".join(re.findall('\d+', districtPhoneWithTitle.group(0)))
		print districtPhone

	def getMailto():
		for a in contactInfoHTML.findAll('a'):
			if 'mailto' in a['href']:
	  			email = a.get('href')[7:]
	  			if email:
	  				print email
	  			else: 
	  				print "no email found"

	districtNumber += 1
