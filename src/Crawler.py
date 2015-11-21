import os, sys

import urllib.request

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from WebPage import WebPage

class SpiderCrawler(object):
    def __init__(self, url, layers = 1):
        self.url = url
        self.layers = layers
        self.pages = []
    def start(self):
        response = urllib.request.urlopen(self.url)
        page = WebPage(response.read())
        self.pages.append(page)
