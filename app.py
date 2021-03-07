import urllib.request
from bs4 import BeautifulSoup

headlines = []

class Scraper:
    def __init__(self, site):
        self.site = site
        self.headlines = []

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            self.headlines.append(url)
    def calculate_precentage(self, topics):
        num = 0
        for i in self.headlines:
            for topic in topics:
                if topic in i:
                    num += 1

        precentage = (num / len(self.headlines)) * 100
        print(str(format(precentage, ".2f")) + "%")
           
scrape = Scraper('https://www.nytimes.com/international/')
scrape.scrape()
test = ["corona"]
scrape.calculate_precentage(test)