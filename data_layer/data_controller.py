import pymongo
import certifi

client_willem = "mongodb+srv://willem:nos_scraper_test@cluster0.dgterps.mongodb.net/?retryWrites=true&w=majority"
client_frans = 'mongodb+srv://fransver:minorityreport@cluster0.oahzdqm.mongodb.net/?retryWrites=true&w=majority'


class DataController:

    def __init__(self):
        self.ca = certifi.where()
        self.client = pymongo.MongoClient(client_frans, tlsCAFile=self.ca)
        self.db = self.client["Articles"]
        self.collection = self.db["NOS"]

    def upload_article_to_database(self, article):
        self.collection.insert_one(article)

    def upload_list_of_articles_to_database(self, articles):
        self.collection.insert_many(articles)

    def delete_all_articles(self):
        self.collection.delete_many({})
