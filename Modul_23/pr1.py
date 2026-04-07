import requests
from bs4 import BeautifulSoup

import pandas as pd
url = f'https://www.kinoafisha.info/news/'
r = requests.get(url)

response = requests.get(url).text
print (response)
soup = BeautifulSoup(r.text, 'lxml')
with open('kinoafisha.info.html', 'w', encoding='utf-8') as output_file:
   output_file.write(r.text)

entries = soup.find_all('a', class_='newsShortList_item grid_cell4')
print (len(entries))

data = []
for entry in entries:
    # Извлекаем дату
    date_tag = entry.find('span', class_='newsShortList_date')
    date = date_tag.get_text(strip=True) if date_tag else "Дата не найдена"

    # Извлекаем название
    name_tag = entry.find("span", class_='newsShortList_title')
    name = name_tag.get_text(strip=True) if name_tag else "Название не найдено"

    # Добавляем в список один словарь с обоими полями
    data.append({
        'data_news': date,
        'name_news': name
    })

print("\nИтоговый список:")
for i, item in enumerate(data, 1):
    print(f"{i}. Дата: {item['data_news']}, Наименование: {item['name_news']}")




