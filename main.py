import time
import datetime
import pandas
from data_controller import DataController
from date_collector import DateCollector
from nos_scraper import NosScraper


if __name__ == '__main__':
    dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2022, 10, 1))
    start_time = time.time()
    scraper = NosScraper()
    articles = scraper.scrape(dates, descr=True)
    end_time = time.time()

    scraper_duration = end_time - start_time

    list_of_lists = []
    article_dictionaries = []
    dcontr = DataController()

    for article in articles:
        #Om een Pandas dataframe te gebruiken, moeten de fields in een list geplaatst worden
        list_of_attribute_values = [article.title, article.description, article.url, article.date]
        list_of_lists.append(list_of_attribute_values)
        #Om de articles naar de Database te uploaden, moeten de objecten naar dictionaries geconverteerd worden
        article_dictionaries.append(article.to_dictionary())

    dcontr.upload_list_of_articles_to_database(article_dictionaries)

    # df = pandas.DataFrame(data=list_of_lists, columns=['Title', 'Description', 'Url', 'Date'])
    # df.to_csv('CSV/Articles_dataframe.csv', index=False)
    #
    # print(df)

    print(f"\nThe duration of the scraping process was: {scraper_duration} seconds for {len(articles)} articles on {len(dates)} page.")
