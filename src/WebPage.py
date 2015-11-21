from XML import XMLTree

class WebPage(object):
    def __init__(self, html):
        self.rawHTML = html
        self.parse()
        
    def parse(self):
        print("Parsing page")
