import csv
import requests
import re
import bs4
from os.path import basename, splitext

from BeautifulSoup import BeautifulSoup

districtNumber = 1

while districtNumber <= 51:

	url = 'http://council.nyc.gov/d%d/html/members/home.shtml' % (districtNumber)
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)

	imageHTML = soup.find('td', attrs={'class' : 'inside_top_image'})
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

	def getImageData():
	 	if  imageHTML:
	 		for img in imageHTML.findAll('img'):
	 			memberName = img.get('alt')
    			img['src'] = splitext(img['src'])[0]
    			imageURL =  'http://council.nyc.gov/d%d/%s.jpg' % (districtNumber, img['src'][6:])
    			print imageURL
	 	else: 
	 		print 'no imageHTML'

	districtNumber += 1
