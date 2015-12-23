import csv
import requests
import re
from tqdm import tqdm
from os.path import basename, splitext
from BeautifulSoup import BeautifulSoup

list_of_leg_phones = []
list_of_dis_phones = []
list_of_emails = []
list_of_names = []
list_of_imageURLs = []

list_of_districts = range(1,52)

def writeToFile():
	list_of_lists = [list_of_names, list_of_imageURLs, list_of_leg_phones, list_of_dis_phones, list_of_emails]
	zipped_list = zip(*list_of_lists)
	outfile = open("./members.csv", "wb")
	writer = csv.writer(outfile)
	writer.writerows(zipped_list)

for districtNumber in tqdm(list_of_districts):

	url = 'http://council.nyc.gov/d%d/html/members/home.shtml' % (districtNumber)
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)

	imageHTML = soup.find('td', attrs={'class' : 'inside_top_image'})
	contactInfoHTML = soup.find('td', attrs={'class' : 'nav_text'})
	contactInfo = contactInfoHTML.text.replace('&nbsp;', '')

	def getLegislativePhone():
		legislativePhoneWithTitle = re.search("((Legislative Office Phone)+.{14})", contactInfo)
		legislativePhone = "".join(re.findall('\d+', legislativePhoneWithTitle.group(0)))
		list_of_leg_phones.append(legislativePhone)

	def getDistrictPhone():
		districtPhoneWithTitle = re.search("((District Office Phone)+.{24})", contactInfo)
		districtPhone = "".join(re.findall('\d+', districtPhoneWithTitle.group(0)))
		list_of_dis_phones.append(districtPhone)

	def getMailto():
		for a in contactInfoHTML.findAll('a'):
			if 'mailto' in a['href']:
	  			email = a.get('href')[7:]
	  			if email:
	  				list_of_emails.append(email)
	  			else: 
	  				list_of_emails.append('n/a')

	def getImageData():
	 	if  imageHTML:
	 		for img in imageHTML.findAll('img'):
	 			memberName = img.get('alt')
    			img['src'] = splitext(img['src'])[0]
    			imageURL =  'http://council.nyc.gov/d%d/%s.jpg' % (districtNumber, img['src'][6:])
    			list_of_imageURLs.append(imageURL)
    			list_of_names.append(memberName)
	 	else: 
	 		list_of_imageURLs.append('n/a')
	 		list_of_names.append('n/a')

	getImageData()
	getLegislativePhone()
	getDistrictPhone()
	getMailto()

writeToFile() 		



	
