import requests
import time
import datetime
import pandas as pd

from date_collector import DateCollector
from article import Article
from bs4 import BeautifulSoup

dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2022, 10, 5))
list_of_lists = []


# https://edition.cnn.com/articles

class CnnScraper:

    def __init__(self):
        self.articles = []
        self.req = requests
        self.soup = BeautifulSoup

    def scrape(self, dates_cnn, descr=True):

        for date in dates_cnn:
            # Datum zit al inn de url van de artikelen, dus die format kon ik hier weglaten.
            url = "https://edition.cnn.com/articles/"
            soup = self.soup(self.req.get(url).content, 'html.parser')
            titles = soup.find_all('h3', class_='cd__headline')
            # urls = soup.find_all('h3', class_='cd__headline') # Kan weg omdat url in zelfde class zit.
            # heb die aangeroepen door in de for alleen het a component aan te roepen.

            for i in range(len(titles)):
                title = titles[i].text
                url = "".join(["https://edition.cnn.com/articles", titles[i].a['href']]) # a class geselecteerd

                if descr:
                    description = self.get_description(url)
                else:
                    description = ""

                article_cnn = Article(title, date, url, description)
                self.articles.append(article_cnn)

        return self.articles

    def get_description(self, url):
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser').head
        description = soup.select_one('meta[name="description"]').attrs['content']

        return description

    def check_if_field_is_empty(self):
        pass


scraper_cnn = CnnScraper()

if __name__ == '__main__':

    articles = scraper_cnn.scrape(dates, descr=False)

    for article in articles:
        list_of_attribute_values = [article.title, article.description, article.date, article.url]
        list_of_lists.append(list_of_attribute_values)
        print(f"title: {article.title}\ndate: {article.date}\ndescription: {article.description}\nurl: {article.url}\n")
