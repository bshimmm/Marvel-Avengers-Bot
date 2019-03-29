"""
avenger scraping for avenger-bot
"""
import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://www.shutterstock.com/search/avengers'

page = requests.get(url)
soup = bs(page.text, 'html.parser')

image_tags = soup.findAll('img')

if not os.path.exists('avengers'):
	os.makedirs('avengers')

os.chdir('avengers')

x = 0

for image in image_tags:
	try:
		url = image['src']
		response = requests.get(url)
		if response.status_code == 200:
			with open('avengers-' + str(x) + '.jpg', 'wb') as f:
				f.write(requests.get(url).content)
				f.close()
				x += 1
	except:
		pass