import csv
import requests
import re
import bs4
from os.path import basename, splitext

from BeautifulSoup import BeautifulSoup

districtNumber = 1

list_of_leg_phones = []
list_of_dis_phones = []
list_of_emails = []
list_of_names = []
list_of_imageURLs = []

while districtNumber <= 3:

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
		list_of_leg_phones.append(legislativePhone)
		print list_of_leg_phones


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

	getLegislativePhone()
	districtNumber += 1 		

def writeToFile():
	outfile = open("./members.csv", "wb")
	writer = csv.writer(outfile)
	writer.writerow(["Name", "LegPhone", "DisPhone", "Email", "imageURL"])


	
