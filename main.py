import sys

from src.Crawler import SpiderCrawler

numArgs = len(sys.argv)

if numArgs < 2:
    print("Please supply a root webpage")
elif numArgs < 3:
    crawler = SpiderCrawler(sys.argv[1], float("+inf"))
    crawler.crawl()
else:
    crawler = SpiderCrawler(sys.argv[1], int(sys.argv[2]))
    crawler.crawl()
