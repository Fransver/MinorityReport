import json
import time
import pandas as pd

from newsapi import NewsApiClient  # Api direct vanaf documentatie

newsapi = NewsApiClient(api_key='43136ce0aa7047fd83aa71a25633260f')

# ================ Api Calls
# to= data meegeven
# q = onderwerp meegeven
# qintitle = titel in artikel zoeken

sources = newsapi.get_top_headlines(sources='bbc-news')  # BBC Top Artikelen
bitcoin = newsapi.get_everything(q='bitcoin')  # Krijgt alles over geselecteerd onderwerp.
top_us = newsapi.get_top_headlines(country="us")
ukrain_news = newsapi.get_everything(qintitle='Ukraine')

# ================= Dataframes
df_bitcoin = pd.DataFrame(data=bitcoin)  # Naar panda Data
df_topus = pd.DataFrame(data=top_us)
df_ukrain_news = pd.read_json(ukrain_news)

# ================== Json dumps


if __name__ == '__main__':
    start_time = time.time()
    print(ukrain_news)
    end_time = time.time()
    duration = end_time - start_time
    print(duration)
