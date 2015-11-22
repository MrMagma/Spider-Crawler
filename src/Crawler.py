import os, sys

import urllib.request

from WebPage import WebPage

def filterUrl(url):
    return (len(url) > 0 and not url[0] == "#")
    
def genMapUrlFn(baseUrl):
    def mapUrl(url):
        if url[0] == "/":
            url = baseUrl + url
        return url
    return mapUrl

class SpiderCrawler(object):
    def __init__(self, url, layers = 1):
        self.url = url
        self.layers = layers
        self.pages = []
    def start(self):
        response = urllib.request.urlopen(self.url)
        page = WebPage(response.read(), filterUrl = filterUrl, mapUrl = genMapUrlFn(self.url))
        for link in page.links:
            print(link)
        self.pages.append(page)
