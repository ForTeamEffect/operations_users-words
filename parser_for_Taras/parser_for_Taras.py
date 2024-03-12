import json
import re
import pprint
import traceback

import requests
from bs4 import BeautifulSoup
import html

partners = dict()
circle = 0


def split_it(nomer):
    new_number = ''
    if nomer:
        for t in nomer:
            try:
                if int(t):
                    new_number = new_number + str(t)
            except Exception as e:
                pass
    return new_number


def get_text(url, page, counter):
    """Парсим конкретный url"""
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    params = {'page_n': page}
    position = 12 * counter
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == 200:
        html_content = BeautifulSoup(res.text, 'html.parser')
        divs = html_content.find_all('div', class_='bp-partner-list-item-name-cnr')
        for div in divs:

            # Очистка текста от HTML-сущностей
            name = html.unescape(div.get_text())
            string = html.unescape(div)
            cut_str = str(string)[str(string).find('href="') + 6:]
            cut_str2 = cut_str[:cut_str.find('">')]
            exactly = requests.get('https://www.bitrix24.ru' + cut_str2, headers=headers)
            html_content = BeautifulSoup(exactly.text, 'html.parser')
            divsss = html_content.find_all('div',
                                           class_='bx-partner-detail-description-contacts-content js-contancts-content')
            for _ in divsss:
                position += 1
                string = html.unescape(_)
                text = string.get_text().split('\n')
                # print(text)
                partners[position] = {}
                partners[position]['name'] = name.strip()
                partners[position]['url'] = 'https://www.bitrix24.ru' + cut_str2
                for key, value in partners.items():
                    if partners[key]['name'] == name.strip():
                        break
                for strings in text:
                    if ' ' in strings or '@' in strings:
                        if '\t' in strings:
                            try:

                                strings.replace(' ', '')
                                strings = re.sub("\s+", "", strings)
                                partners[position]['email'] = strings or None
                            except Exception:
                                pass
                        if 'Адрес' in strings:
                            try:
                                adr_or_phone = strings.split('Адрес ')
                                partners[position]['address'] = adr_or_phone[1] or None
                            except Exception:
                                pass
                        if 'Телефон' in strings:
                            try:
                                adr_or_phone = strings.split()
                                partners[position]['phone'] = split_it(strings.split('Телефон')[1]) or None
                            except Exception:
                                pass
                        if 'звоните:' in strings:
                            try:
                                partners[position]['phone_bitrix'] = split_it(
                                    strings.split('По Битрикс24 звоните: ')[1]) or None
                            except Exception:
                                pass

        return partners
    else:
        print(f"Error: {res.status_code}")
        return None


counter = 1

while True:
    dictor = get_text(url='https://www.bitrix24.ru/partners/', page=str(counter), counter=counter - 1)
    print(dictor)
    if dictor == {} or counter == 123:
        break
    counter = counter + 1

# p = get_text(url='https://www.bitrix24.ru/partners/', page='100')
#
# print(p)

with open('bitrix_partners.txt', 'a', encoding='UTF-8') as t:
    formatted_data = json.dumps(partners, indent=4, ensure_ascii=False)
    t.write(formatted_data)

if __name__ == '__main__':
    pass
