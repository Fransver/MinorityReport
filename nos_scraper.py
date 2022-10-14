from bs4 import BeautifulSoup, SoupStrainer
import requests
from article import Article
from multiprocessing import Pool


# TODO multiprocessing

class NosScraper:

    def __init__(self):
        self.articles = []
        self.req = requests
        self.soup = BeautifulSoup

    def scrape(self, dates, descr=True):

        for date in dates:
            url = "https://nos.nl/nieuws/archief/{}-{}-{}".format(date.year, date.strftime('%m'), date.strftime('%d'))
            soup = self.soup(self.req.get(url).content, 'html.parser')

            # parent = soup.find_all('li', class_='list-time__item')
            # titles = []
            # urls = []
            # for p in parent:
            #     titles.extend(p.find_all('div', class_='list-time__title'))
            #     urls.extend(p.find_all('a', class_='link-block'))
            # DELETE?

            titles = soup.find_all('div', class_='list-time__title')
            urls = soup.find_all('a', class_='link-block')

            for i in range(len(titles)):
                title = titles[i].contents[0]
                url = "".join(["https://www.nos.nl", urls[i].attrs['href']])

                if descr:
                    description = self.get_description(url)
                else:
                    description = ""

                article = Article(title, url, date, description)
                self.articles.append(article)

        return self.articles

    def get_description(self, url):
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser').head
        description = soup.select_one('meta[name="description"]').attrs['content']

        return description

    def check_if_field_is_empty(self):
        pass
