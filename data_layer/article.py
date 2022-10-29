from dataclasses import dataclass


@dataclass
class Article:
    # id : str
    title: str
    date: str
    url: str
    description: str  # misschien niet nodig in later stadium.
    # tf-idf waarde :

    def to_dictionary(self):
        return {"Title": self.title, "Date": self.date, "url": self.url, "Description": self.description}
