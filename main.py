import time
import datetime

from logical_layer.date_collector import DateCollector
from logical_layer.scrapers.nos_scraper import NosScraper
from logical_layer.scrapers.cnn_scraper import CnnScraper
from data_layer.data_controller import DataController

# ========================= Dates
dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2022, 10, 5))

# ========================= SCRAPERS
scraper_nos = NosScraper()
scraper_cnn = CnnScraper()

# ========================== Lists
list_of_lists = []
mongo_upload_dict = []

# ========================== Database
database_control = DataController()

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
        mongo_article = article.to_dictionary() # omzetten naar dict voor MongoDB
        mongo_upload_dict.append(mongo_article)
        print(f"title: {article.title}\nurl: {article.url}\ndescription: {article.description}\ndate: {article.date}\n")

    # Werkt top! Had in 0.5 sec alle artikelen binnen en in map geschreven.
    # df = pd.DataFrame(data=list_of_lists, columns=['Title', 'Description', 'Url', 'Date'])
    # df.to_csv('CSV/Articles_dataframe.csv', index=False)

    print(f"\nThe duration of the scraping process was: {scraper_duration} seconds "
          f"for {len(articles)} articles on {len(dates)} page.")

    database_control.upload_list_of_articles_to_database(mongo_upload_dict) # upload naar Mongo

    # print(pd.read_csv('CSV/Articles_dataframe.csv'))
