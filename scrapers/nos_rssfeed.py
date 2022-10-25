import datetime
import requests

from bs4 import BeautifulSoup
from scrapers.scraper_interface import BeautifulParent

#============== Lukt niet om Soup en Req te activeren.

class NosRssScraper(BeautifulParent):
    def __int__(self):
        super().__int__()

    def scrape(self, dates_scraper):
        url = 'https://feeds.nos.nl/nosnieuwsbinnenland'
        soup = BeautifulSoup(self.req.get(url).content, 'lxml')
        titles = soup.find_all('a')
        self.articles.append(titles)
        print(titles)


if __name__ == '__main__':
    list_of_lists = []
    scraper_rss = NosRssScraper()
    scraper_rss.scrape(1)
