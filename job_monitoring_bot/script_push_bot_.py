import requests
import schedule
import time

TOKEN = ''
MAIN_URL = ''
BASE_URL = 'https://api.hh.ru/'
CONNECT_TIMEOUT = 60
READ_TIMEOUT = 60
TIME_PUSH = '18:00'
ARR_JOBS = ('python', 'django', 'tornado', 'asyncio', 'aiohttp',
            'javascript', 'react', 'node.js',
            'java', 'string',
            'kotlin',
            'golang')


def get_search_vacancies(text=None):
    """
    Returns all job information by search
    :param text: (str)
    :return: (int)
    """
    url = '{}vacancies?text={}&area=1&from=cluster_area'.format(BASE_URL, text)
    try:
        r = requests.get(url, timeout=(CONNECT_TIMEOUT, READ_TIMEOUT))
    except requests.exceptions.ReadTimeout:
        raise Exception('Истек таймаут чтения')
    except requests.exceptions.ConnectTimeout:
        raise Exception('Истекло время ожидания соединения c сервером')
    except requests.exceptions.ConnectionError:
        raise Exception('Неудалось подключится к серверу')
    except requests.exceptions.HTTPError as err:
        raise Exception('Произошла ошибка HTTP: {}'.format(err.response.content))

    try:
        data = r.json()
    except Exception as arr:
        raise Exception(arr)

    return data


def get_search_count_vacancy(text=None):
    """
    Returns the number of vacancies by search
    :param text: (str)
    :return: (int)
    """
    data = get_search_vacancies(text)
    if isinstance(data, dict):
        return data.get('found')
    else:
        raise Exception('Полученные данные не являются словарем')


def get_search_count_vacancies(name_vacancies):
    """
    Get the number of vacancies for each search.
    :param name_vacancies: (list)
    :return: (dist)
    """
    jobs = {}
    for name_vacancy in name_vacancies:
        count_vacancy = get_search_count_vacancy(name_vacancy)
        jobs.update({name_vacancy: count_vacancy})
    return jobs


def main():
    data = {
        'chat_id': 448781037,
        'text': str(get_search_count_vacancies(ARR_JOBS))
    }
    url = f'{MAIN_URL}/sendMessage'
    requests.get(url, data=data)


if __name__ == "__main__":
    schedule.every().day.at(TIME_PUSH).do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
