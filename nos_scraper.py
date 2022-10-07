from bs4 import BeautifulSoup, SoupStrainer
import requests
from article import Article
from date_collector import DateCollector
import datetime


# TODO multithreading

class NosScraper:

    def scrape(self, dates, descr=True):
        articles = []

        for date in dates:
            url = "https://nos.nl/nieuws/archief/{}-{}-{}".format(date.year, date.strftime('%m'), date.strftime('%d'))
            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')

            parent = soup.find_all('li', class_='list-time__item')
            # titles = []
            # urls = []
            # for p in parent:
            #     titles.extend(p.find_all('div', class_='list-time__title'))
            #     urls.extend(p.find_all('a', class_='link-block'))

            titles = soup.find_all('div', class_='list-time__title')
            urls = soup.find_all('a', class_='link-block')

            for x in range(len(titles)):
                title = titles[x].contents[0]
                url = "".join(["https://www.nos.nl", urls[x].attrs['href']])

                if descr:
                    description = self.get_description(url)
                else:
                    description = ""

                article = Article(title, url, date, description)
                articles.append(article)

        return articles


    def get_urls(self, dates):
        search_urls = []

        for date in dates:
            search_urls.append(
                "https://nos.nl/nieuws/archief/{}-{}-{}".format(date.year, date.strftime('%m'), date.strftime('%d')))

        return search_urls

    def get_description(self, url):
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser').head
        description = soup.select_one('meta[name="description"]').attrs['content']

        return description
