import requests
import datetime

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from better_abc import ABCMeta, abstract_attribute


class Scraper(ABC):
    def __int__(self, dates):
        self.articles = []
        self.dates = 4

    @abstractmethod
    def scrape(self):
        pass


class BeautifulParent(Scraper):
    def __int__(self, dates):
        super().__init__(dates)
        self.soup = BeautifulSoup
        self.req = requests

    def scrape(self, description=True):
        print('parent is oke')


class NewYorkTimesScraper(BeautifulParent):
    def __int__(self, dates):
        super().__init__()

    def scrape(self, description=True):
        print('child oke')


if __name__ == '__main__':
    scraper = NewYorkTimesScraper()
