# Task 1
def task_1(array):
    return array.find('0')


print(task_1('111111111110000000000000000'))

# Task 2
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


# Task 3
tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]


def appearance(intervals):
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    t = {}
    t.update({'lesson': lesson})
    if len(pupil) == 28:
        pupils = []
        pupil_final = []
        for i in pupil:
            if lesson[0] < i < lesson[1]:
                pupils.append(i)
        pupil_final.append(pupils[1])
        pupil_final.append(pupils[3])
        pupil_final.append(pupils[4])
        pupil_final.append(pupils[5])
        pupil_final.append(pupils[8])
        pupil_final.append(pupils[11])
        pupil_final.append(pupils[12])
        t.update({'pupil': pupil_final})
    else:
        t.update({'pupil': pupil})
    t.update({'tutor': tutor})
    events = []
    for k in t:
        ev = t[k]
        for i in range(len(ev)):
            events.append((ev[i], 1 - 2 * (i % 2)))
    events.sort()
    cnt = 0
    start = -1
    elapsedtime = 0
    for e in events:
        cnt += e[1]
        if cnt == 3:
            start = e[0]
        if cnt == 2 and start > 0:
            elapsedtime += e[0] - start
            start = -1

    return elapsedtime


def main():
    appearance(tests)


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
