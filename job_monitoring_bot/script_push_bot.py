import os
import sys
import requests
import schedule
import time

from config import MAIN_URL

from hh.logic import get_search_count_vacancies

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)


BASE_URL = 'https://api.hh.ru/'
CONNECT_TIMEOUT = 60
READ_TIMEOUT = 60
TIME_PUSH = '18:00'
ARR_JOBS = ('python', 'django', 'tornado', 'asyncio', 'aiohttp',
            'javascript', 'react', 'node.js',
            'java', 'string',
            'kotlin',
            'golang')


def main():
    data = {
        'chat_id': 448781037,
        'text': str(get_search_count_vacancies(ARR_JOBS))
    }
    url = f'{MAIN_URL}/sendMessage'
    requests.get(url, data=data)


# if __name__ == "__main__":
#     schedule.every().day.at(TIME_PUSH).do(main)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


if __name__ == "__main__":
    print('RUN')
    while True:
        print('GO')
        main()
        time.sleep(10)
