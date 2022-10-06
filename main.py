import time
import datetime

from date_collector import DateCollector
from nos_scraper import NosScraper

dates = DateCollector().get_range_of_dates(starting_date=datetime.date(2010, 1, 1))

start_time = time.time()
scraper = NosScraper()
articles = scraper.scrape(datetime.date(2022, 1, 1))
end_time = time.time()

scraper_duration = end_time - start_time

print("SCRAPER RESULTS\n")

for article in articles:
    print(f"title: {article.title}")
    print(f"url: {article.url}")
    print(f"date: {article.date}")
    print(f"description: {article.description}\n")

print(f"\nThe duration of the scraping process was: {scraper_duration} seconds for {len(articles)} articles on one page.")