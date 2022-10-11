from dataclasses import dataclass


@dataclass
class Article:
    title: str
    date: str
    url: str
    description: str
