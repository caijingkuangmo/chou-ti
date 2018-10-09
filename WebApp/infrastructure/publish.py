# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import requests
from bs4 import BeautifulSoup

def get_url_title(url):
    '''
    获取网页标题
    :param url:
    :return:
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.title.text
