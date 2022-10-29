from data_layer.article import Article
from logical_layer.scrapers.scraper_interface import BeautifulParent


class NosScraper(BeautifulParent):
    def __init__(self):
        super().__init__()
        self.url = "https://nos.nl/nieuws/archief/{}-{}-{}"

    def scrape(self, dates, descr=True):

        for date in dates:
            url = self.url.format(date.year, date.strftime('%m'), date.strftime('%d'))
            soup = self.soup(self.req.get(url).content, 'html.parser')
            titles = soup.find_all('div', class_='list-time__title')
            urls = soup.find_all('a', class_='link-block')

            for i in range(len(titles)):
                title = titles[i].contents[0]
                url = "".join(["https://www.nos.nl", urls[i].attrs['href']])

                if descr:
                    description = self.get_description(url)
                else:
                    description = ""

                article = Article(title, date, url, description)
                self.articles.append(article)

        return self.articles

    def get_description(self, url):
        req = self.req.get(url)
        soup = self.soup(req.content, 'html.parser').head
        description = soup.select_one('meta[name="description"]').attrs['content']

        return description

    def check_if_field_is_empty(self):
        pass
