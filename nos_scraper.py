from bs4 import BeautifulSoup
import requests
from article import Article
from date_collector import DateCollector
import datetime


class NosScraper:

    def scrape(self, date):
        articles = []

        # for page in self.get_urls(dates):
        # req = requests.get(page)
        url = "https://nos.nl/nieuws/archief/{}-{}-{}".format(date.year, date.strftime('%m'), date.strftime('%d'))
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        parent = soup.find_all('li', class_='list-time__item')
        titles = []
        urls = []
        for p in parent:
            titles.extend(p.find_all('div', class_='list-time__title'))
            urls.extend(p.find_all('a', class_='link-block'))

        # titles = soup.find_all('div', class_='list-time__title')
        # urls = soup.find_all('a', class_='link-block')

        for x in range(len(titles)):
            title = titles[x].contents[0]
            url = "".join(["https://www.nos.nl", urls[x].attrs['href']])
            description = self.get_description(url)
            # description = ""

            article = Article(title, url, date, description)
            articles.append(article)

        return articles

    # def scrape(self, dates):
    #     articles = []
    #
    #     # for page in self.get_urls(dates):
    #     # req = requests.get(page)
    #     req = requests.get('https://nos.nl/nieuws/archief/2021-01-01')
    #     soup = BeautifulSoup(req.content, 'html.parser')
    #
    #     titles = soup.find_all('div', class_='list-time__title')
    #     urls = soup.find_all('a', class_='link-block')
    #
    #     for x in range(len(titles)):
    #         title = titles[x].contents[0]
    #         url = "".join(["https://www.nos.nl", urls[x].attrs['href']])
    #         date = datetime.date(2021, 1, 1)
    #         # description = self.get_description(url)
    #         description = ""
    #
    #         article = Article(title, url, date, description)
    #         articles.append(article)
    #
    #     return articles


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
