from bs4 import BeautifulSoup

# rewrites = {
#     " ": "//",
#     ">": "/",
#     "^": "..",
#     "&": "."
# }

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
        return matched
    def get(self, attr, defaultVal = None):
        if attr not in self._tree.attrs:
            return defaultVal
        return self._tree[attr]
    def _findByCSS(self, selector):
        # TODO (Joshua): Reimplement CSS style selectors
        # for css, xpath in rewrites:
        #     selector = selector.replace(css, xpath)
        return self._tree.find_all(selector)

class XMLTree(XMLNode):
    def __init__(self, content):
        self.content = content
        self._tree = BeautifulSoup(content, "html.parser")
