import datetime

from logical_layer.scrapers.scraper_interface import BeautifulParent


# ============== Lukt niet om Soup en Req te activeren.

class NosRssScraper(BeautifulParent):
    def __init__(self):
        super().__init__()
        self.url = "https://edition.cnn.com/articles/"

    def scrape(self, dates_scraper):
        soup = self.soup(self.req.get(self.url).content, 'html.parser')
        titles = soup.find_all('h3', class_='cd__headline')
        self.articles.append(titles)
        print(titles)
        return self.articles


if __name__ == '__main__':
    titles = []
    today = datetime.date.today()
    scraper_rss = NosRssScraper()
    scraper_rss.scrape(today)
