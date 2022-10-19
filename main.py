import time
import datetime
import pandas as pd

from date_collector import DateCollector
from nos_scraper import NosScraper
from cnn_scraper import CnnScraper

# ========================= Dates
dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2022, 10, 5))

# ========================= SCRAPERS
scraper_nos = NosScraper()
scraper_cnn = CnnScraper()

# ========================== Lists
list_of_lists = []

if __name__ == '__main__':
    start_time = time.time()
    # ===================================================== Keuze welke Scraper
    # articles = scraper_nos.scrape(dates, descr=False)  #NOS
    articles = scraper_cnn.scrape(dates, descr=False)    #CNN

    end_time = time.time()

    scraper_duration = end_time - start_time

    for article in articles:
        list_of_attribute_values = [article.title, article.description, article.url, article.date]
        list_of_lists.append(list_of_attribute_values)
        print(f"title: {article.title}\nurl: {article.url}\ndescription: {article.description}\ndate: {article.date}\n")

    # Werkt top! Had in 0.5 sec alle artikelen binnen en in map geschreven.
    # df = pd.DataFrame(data=list_of_lists, columns=['Title', 'Description', 'Url', 'Date'])
    # df.to_csv('CSV/Articles_dataframe.csv', index=False)

    print(f"\nThe duration of the scraping process was: {scraper_duration} seconds "
          f"for {len(articles)} articles on {len(dates)} page.")

    # print(pd.read_csv('CSV/Articles_dataframe.csv'))
