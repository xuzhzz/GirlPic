import requests
from requests.exceptions import ConnectionError
from lxml import etree


class GetImg(object):
    img_urls = []
    # url = 'http://www.mzitu.com/[0-9]+'
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Referer': 'http://www.mzitu.com/',
        }
        self.html = self.get_html(url)

    def get_html(self, url):
        if url is None:
            print('use %s' % self.url)
            url = self.url
        try:
            response = requests.get(url=url, headers=self.headers)
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            print('get_html connection error!')

    def pages_count(self, html):
        select = etree.HTML(html)
        return select.xpath('//*[@class="pagenavi"]/a[last()-1]/span')[0].text

    def parse_img_urls(self, url):
        html = self.get_html(url)
        select = etree.HTML(html)
        res = select.xpath('/html/body/div[@class="main"]/div[@class="content"]/div[@class="main-image"]//img/@src')
        if res is not None:
            for item in res:
                # print('find a image %s' % item)
                self.img_urls.append(item)

    # 获取套图名字
    def get_name(self):
        select = etree.HTML(self.html)
        return select.xpath('/html/body/div[@class="main"]/div[@class="content"]/h2[@class="main-title"]')[0].text

    # 获取套图标签
    def get_tag(self):
        select = etree.HTML(self.html)
        return select.xpath("/html/body/div[@class='main']/div[@class='content']/div[@class='main-meta']/span[1]/a")[0].text

    # 获取套图中所有图片的链接，返回一个链接的集合
    def get_img(self):
        # first_page_html = self.get_html(self.url)
        count = int(self.pages_count(self.html))
        slash = ''
        if self.url[-1] is not '/':
            slash = '/'
        for index in range(1, count+1):
            per_page = self.url + slash + str(index)
            self.parse_img_urls(per_page)
        return self.img_urls
