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
        self.startUrl = url
        self.layers = layers
        self.pages = []
        self.crawled = []
        self.notCrawled = [url]
    def crawl(self, layers = None):
        if layers is None:
            layers = self.layers
        if layers > 0:
            crawlThese = self.notCrawled
            self.notCrawled = []
            for link in crawlThese:
                self.crawled.append(link)
                print("Crawling: " + link)
                try:
                    response = urllib.request.urlopen(link)
                except:
                    print("Attempting to fetch URL \"" + link + "\" returned an error")
                    pass
                    continue
                page = WebPage(response, filterUrl, genMapUrlFn(link))
                self.pages.append(page)
                for toCrawl in page.links:
                    if toCrawl not in self.crawled:
                        self.notCrawled.append(toCrawl)
            self.crawl(layers - 1)
