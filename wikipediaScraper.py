                # Importing important libraries:

import requests
from bs4 import BeautifulSoup


                # Input for scraping link

n = input('Enter topic you want to search: ').replace(' ','+')
modified = 'https://www.google.com/search?q='+n+'+wikipedia'
response = requests.get(modified)


                # Modifying link 

soup = BeautifulSoup(response.text,'html.parser')
link = 'Not found on wikipedia'
for i in soup.findAll('a'):
    if 'https://en.wikipedia.org/wiki/' in i.get('href'):
        link = i.get('href')[7:].split('&')[0]
        break

                # Processing request for extraction 

res = requests.get(link)
soup = BeautifulSoup(res.text,'html.parser')

corpus = ''
for p in soup.find_all('p'):
    corpus += p.text
    corpus += '\n'
    
corpus = corpus.strip()

for i in range(500):
    corpus = corpus.replace('['+str(i)+']','')

                # printing paragraph 
print(corpus)