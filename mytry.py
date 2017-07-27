# import requests
# from requests.exceptions import ConnectionError
# import re
# from lxml import etree
# from getImg import GetImg
# import os
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
#     'Referer': 'http://www.mzitu.com/',
# }
#
# resp = requests.get('http://www.mzitu.com/13181/6', headers=headers)
#
# select = etree.HTML(resp.text)
#
# print(select.xpath('/html/body/div[@class="main"]/div[@class="content"]/div[@class="main-image"]//img/@src'))
#
# url = 'http://www.mzitu.com/13181'
# imgs = GetImg(url)
# res = imgs.get_img()
# print(res)
# print(imgs.get_tag())
# print(imgs.get_name())