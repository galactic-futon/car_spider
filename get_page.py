from requests import get
import csv
from time import sleep
from random import randint
from time import time
from bs4 import BeautifulSoup
import re
import numpy as np

site = get('https://sandiego.craigslist.org/search/cta?hasPic=1&min_price=500&max_price=5000&hasPic=1')    
html_soup = BeautifulSoup(site.text, 'html.parser')

results_num = html_soup.find('div', class_ = 'search-legend')
results_total = int(results_num.find('span', class_ = 'totalcount').text)

pages = np.arange(0, results_total+1, 120)

with open("output.csv", "w", newline='') as csvfile:
    for page in pages: 

        currPage = "%s%s%s%s%s" % ("https://sandiego.craigslist.org/search/cta?","s=", page, "&hasPic=1", "&min_price=500&max_price=5000")
        response = get(currPage)
        sleep(randint(1,5))
        toParse = BeautifulSoup(response.text, 'html.parser')
        posts = toParse.find_all('li', class_='result-row')

        #begin post data point definitions
        prices = (post.span.text for post in posts)
        photoLinks = (post.find('a', class_='result-image gallery')['href'] for post in posts)
        datesPosted = (post.find('time', class_='result-date').text for post in posts)
        carTitles = (post.find('a', class_='result-title').text for post in posts)

        
        dataset = [(x,y,z,a) for x, y, z, a  in zip(prices, carTitles, datesPosted, photoLinks)]
        
        writer = csv.writer(csvfile)
        for data in dataset:
            writer.writerow(data)
