import requests
from bs4 import BeautifulSoup

url = f'https://www.kinoafisha.info/selections/theater/'
r = requests.get(url)

response = requests.get(url).text
print (response)

soup = BeautifulSoup(r.text, 'lxml')
with open('kinoafisha.html', 'w', encoding='utf-8') as output_file:
   output_file.write(r.text)

entries = soup.find_all('div', class_='compilationList_item grid_cell')
print (len(entries))












