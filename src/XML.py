import xml.etree.ElementTree as ElementTree

rewrites = {
    " ": "//",
    ">": "/",
    "^": "..",
    "&": "."
}

class XMLNode(object):
    def __init__(self, elTree):
        self._tree = elTree
    def find(self, selector):
        selector = selector.split(",")
        matched = []
        for cssSelector in selector:
            matched.extend(self._findByCSS(cssSelector))
        for i in range(0, len(matched)):
            matched[i] = XMLNode(matched[i])
    def _findByCSS(self, selector):
        for css, xpath in rewrites.iteritems():
            selector = selector.replace(css, xpath)
        return self._tree.findall(selector)

class XMLTree(XMLNode):
    def __init__(self, content):
        self.content = content
        self._tree = ElementTree.fromstring(content)
