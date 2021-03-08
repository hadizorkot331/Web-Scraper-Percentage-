import urllib.request
from bs4 import BeautifulSoup
import numpy as np


class Scraper:
    def __init__(self, site):
        self.site = site
        self.headlines = np.array([])

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.getText()
            self.headlines = np.append(self.headlines, url)
            
    def calculate_precentage(self, topics):
        num = 0
        for i in self.headlines:
            for topic in topics:
                if topic.lower() in i.lower():
                    num += 1

        precentage = (num / len(self.headlines)) * 100
        print(str(format(precentage, ".2f")) + "%")
           
scrape = Scraper('https://www.nytimes.com/international/')
scrape.scrape()
test = ["Vaccine"]
scrape.calculate_precentage(test)