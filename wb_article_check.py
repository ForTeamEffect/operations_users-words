import requests


def parse(article, word):
    params = {'TestGroup': 'no_test',
              'TestID': 'no_test',
              'appType': '1',
              'curr': 'rub',
              'dest': '-1257786',
              'query': word,
              'resultset': 'catalog',
              'sort': 'popular',
              'spp': '29',
              'suppressSpellcheck': 'false'}
    api_url = 'https://search.wb.ru/exactmatch/ru/common/v4/' \
              f'search?'
    headers = {
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    response = requests.get(api_url, headers=headers, params=params)
    # response.raise_for_status()
    data = response.json().get('data')['products']
    for i in range(0, 99):
        if data[i].get('id') == article:
            return f'позиция {i + 1}'


word = 'gta6'
article = 194601263

print(parse(article, word))