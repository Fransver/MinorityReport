from dataclasses import dataclass


@dataclass
class Article:
    title: str
    date: str
    url: str
    description: str

    def to_dictionary(self):
        return {"Title": self.title, "Date": self.date, "url": self.url, "Description": self.description}
