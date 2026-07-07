import urllib.request
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.links.append(v)

def scrape_links(url):
    with urllib.request.urlopen(url) as r:
        html = r.read().decode()
    p = LinkParser()
    p.feed(html)
    return p.links
