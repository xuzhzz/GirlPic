import requests
from requests.exceptions import ConnectionError
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Referer': 'http://www.mzitu.com/',
}

# 获取所有套图的URL
def get_all(url):
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            pattern = re.compile('(http://www.mzitu.com/[0-9]+)')
            return pattern.findall(response.text)
    except ConnectionError:
        print('get all urls connection error!')



if __name__ == '__main__':
    all_urls = get_all('http://www.mzitu.com/all/')
    print(all_urls)
