from XML import XMLTree

class WebPage(XMLTree):
    def __init__(self, content, filterUrl = lambda: True, mapUrl = lambda url: url):
        super(WebPage, self).__init__(content)
        self.links = map(mapUrl, filter(filterUrl, map(lambda el: el.get("href", ""), self.find("a"))))
