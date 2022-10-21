import requests
import datetime
import data.date_collector

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from data.date_collector import DateCollector


# De verplichting van data komt pas in de methode terug.
# Volgens mij gebruik je een interface ook alleen maar als blauwdruk voor welke verplichte methodes erin zitten.
# De attributen kunnen per implementatie van de interface verschillen. Die moet je dus loskoppelen.
# In de BeautifulParent heb ik nu aangegeven dat het een lijst moet zijn van dates. Zoals datacollector aangeeft.

class Scraper(ABC):
    @abstractmethod
    def scrape(self, **kwargs):
        pass


class BeautifulParent(Scraper):
    def __int__(self):
        super().__init__()
        self.soup = BeautifulSoup
        self.req = requests

    def scrape(self, dates_scraper):
        pass


class NewYorkTimesScraper(BeautifulParent):
    def __int__(self):
        super().__init__()

    def scrape(self, dates_scraper, description=True):

        for date in dates_scraper:
            print(date)


if __name__ == '__main__':
    dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2022, 10, 5))
    scraper = NewYorkTimesScraper()
    scraper.scrape(dates)
