import time
import datetime
import pandas

from date_collector import DateCollector
from nos_scraper import NosScraper

if __name__ == '__main__':
    dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2022, 10, 5))
    start_time = time.time()
    scraper = NosScraper()
    articles = scraper.scrape(dates, descr=False)
    end_time = time.time()

    scraper_duration = end_time - start_time
    list_of_lists = []

    for article in articles:
        list_of_attribute_values = [article.title, article.description, article.url, article.date]
        list_of_lists.append(list_of_attribute_values)

    df = pandas.DataFrame(data=list_of_lists, columns=['Title', 'Description', 'Url', 'Date'])
    df.to_csv('CSV/Articles_dataframe.csv', index=False)

    print(df)
    print(f"\nThe duration of the scraping process was: {scraper_duration} seconds for {len(articles)} articles on {len(dates)} page.")
