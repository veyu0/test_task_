
import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaBrowser/22.5.0.1884 Yowser/2.5 Safari/537.36"
}
url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

req = requests.get(url, headers=headers).text
order = {}
while True:
    soup = BeautifulSoup(req, 'lxml')

    block = soup.find('div', class_='mw-category mw-category-columns')
    category_letter = block.find('div', class_='mw-category-group')
    category = category_letter.find_next('h3').text
    animal_names = block.find_all('li')

    animals_names = []
    for animal in animal_names:
        animal_name = animal.text
        animals_names.append(animal_name)

    names = 0
    for name in animals_names:
        if name.startswith(category):
            names += 1
    names_dict = {}
    names_dict.update({category: names})

    for key in names_dict:
        try:
            order[key] += int(names_dict[key])
        except:
            order[key] = int(names_dict[key])

    links = soup.find('div', id='mw-pages').find_all('a')
    for a in links:
        if a.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + a.get('href')
            req = requests.get(url).text
            break
    else:
        break

for key, value in order.items():
    print(key, value)
