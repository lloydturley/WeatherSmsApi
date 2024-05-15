import requests
from Article import Article


class NewsMonitor:
    def __init__(self):
        self.articles = []

    def initialize_articles(self, api_key, quantity=5):
        parameters = {
            "country" : "us",
            "category" : "business",
            "apiKey": api_key,
            "pageSize": quantity,
            "language": "en",
        }

        response = requests.get("https://newsapi.org/v2/top-headlines", params=parameters)
        response.raise_for_status()
        received_articles = response.json()["articles"]

        for article in received_articles:
            article_instance = Article(
                title=article["title"],
                description=article["description"],
                url=article["url"]
            )
            self.articles.append(article_instance)
