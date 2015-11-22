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
    def __init__(self, url, layers = 1, output = None):
        self.startUrl = url
        self.layers = layers
        self.crawled = []
        self.notCrawled = [(url, "START")]
        if output is not None:
            self.output = open(output, "a")
            self.output.write("[\n")
    def crawl(self, layers = None):
        if layers is None:
            layers = self.layers
        if layers > 0:
            crawlThese = self.notCrawled
            self.notCrawled = []
            for link, cameFrom in crawlThese:
                self.crawled.append(link)
                print("Crawling: " + link)
                try:
                    response = urllib.request.urlopen(link)
                except:
                    print("Attempting to fetch URL \"" + link + "\" returned an error")
                    pass
                    continue
                page = WebPage(response, filterUrl, genMapUrlFn(link))
                jsonLinks = "[\n"
                for toCrawl in page.links:
                    jsonLinks += ("    " * 3) + "\"" + toCrawl + "\",\n"
                    if toCrawl not in self.crawled:
                        self.notCrawled.append((toCrawl, link))
                jsonLinks += ("    " * 2) + "]"
                if hasattr(self, "output"):
                    json = ("    " * 1) + "{\n" + ("    " * 2) + "\"url\": \"" + link + "\",\n" + ("    " * 2)
                    json += "\"leadsTo\": " + jsonLinks + ",\n" + ("    " * 2) + "\"cameFrom\": \"" + cameFrom + "\"\n" + ("    " * 1) + "},"
                    self.output.write(json)
                    self.output.write("\n")
            self.crawl(layers - 1)
            if layers == self.layers and hasattr(self, "output"):
                self.output.write("]")
                self.output.close()
                
