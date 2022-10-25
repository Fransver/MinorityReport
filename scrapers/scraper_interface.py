import requests
import datetime

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from data.date_collector import DateCollector


# De verplichting van data komt pas in de methode terug.
# Volgens mij gebruik je een interface ook alleen maar als blauwdruk voor welke verplichte methodes erin zitten.
# De attributen kunnen per implementatie van de interface verschillen. Die moet je dus loskoppelen.
# In de BeautifulParent heb ik nu aangegeven dat het een lijst moet zijn van dates. Zoals datacollector aangeeft.

class Scraper(ABC):   # Hier de blauwdruk van de scraper maken waarin variabel datum-lijst nog optioneel is.
    @abstractmethod
    def scrape(self, *args):
        pass


class BeautifulParent(Scraper): # De Beutiful Soup scrapers gebruiken allemaal de soup en requests. Dus meegegeven.
    def __int__(self):
        super().__init__()
        self.articles = []
        self.soup = BeautifulSoup
        self.req = requests

    def scrape(self, dates_scraper):  # Hier al aangeven dat een Beuautiful Soup Scraper een lijst data moet hebben.
        pass


class NewYorkTimesScraper(BeautifulParent): # Hier met super alles overgedragen vanuit de soup parent.
    def __int__(self):
        super().__init__()

    def scrape(self, dates_scraper, description=True): # Hier eigenlijk pas een daadwerkelijke functie meegegegeven.

        for date in dates_scraper:
            print(date)


if __name__ == '__main__':
    dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2022, 10, 5))
    scraper = NewYorkTimesScraper()
    scraper.scrape(dates)
