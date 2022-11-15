#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
                                            (`-.      ('-.                 _   .-')    _ .-') _ .-. .-')   
                                          _(OO  )_  _(  OO)               ( '.( OO )_ ( (  OO) )\  ( OO )  
  ,-.-')        ,--.      .-'),-----. ,--(_/   ,. \(,------.        ,-.-') ,--.   ,--.)\     .'_ ;-----.\  
  |  |OO)       |  |.-') ( OO'  .-.  '\   \   /(__/ |  .---'        |  |OO)|   `.'   | ,`'--..._)| .-.  |  
  |  |  \       |  | OO )/   |  | |  | \   \ /   /  |  |            |  |  \|         | |  |  \  '| '-' /_) 
  |  |(_/       |  |`-' |\_) |  |\|  |  \   '   /, (|  '--.         |  |(_/|  |'.'|  | |  |   ' || .-. `.  
 ,|  |_.'      (|  '---.'  \ |  | |  |   \     /__) |  .--'        ,|  |_.'|  |   |  | |  |   / :| |  \  | 
(_|  |          |      |    `'  '-'  '    \   /     |  `---.      (_|  |   |  |   |  | |  '--'  /| '--'  / 
  `--'          `------'      `-----'      `-'      `------'        `--'   `--'   `--' `-------' `------'  

'''

"""imdbScraper.py: A web scraper for IMDB to find the Top 250 movies and TV Shows."""

__author__ = "Eric Gutierrez Jr."
__email__ = "dreaded.sushi@gmail.com"
__license__ = "MIT"
__date__= "2022-11-14"
__version__= "1.0.0"
__status__ = "Complete"

# Path: imdbScraper.py
# Output: imdbScraper.csv

# Import libraries
import requests
from bs4 import BeautifulSoup
import csv


# Find the Top 250 movies on IMDB
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
html = response.content

# Parse the HTML for Rank, Title, Year, and Rating
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody', attrs={'class': 'lister-list'})
rows = table.find_all('tr')

# Create a CSV file to store the data
with open('imdbScraper.csv', 'w', newline='') as csvfile:
    fieldnames = ['Rank', 'Title', 'Year', 'Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in rows:
        rank = row.find('td', attrs={'class': 'titleColumn'}).get_text().strip()
        title = row.find('td', attrs={'class': 'titleColumn'}).find('a').get_text()
        year = row.find('td', attrs={'class': 'titleColumn'}).find('span').get_text().strip('()')
        rating = row.find('td', attrs={'class': 'ratingColumn imdbRating'}).get_text().strip()
        writer.writerow({'Rank': rank, 'Title': title, 'Year': year, 'Rating': rating})

# Print to console on completion
print('Scraping Complete')
