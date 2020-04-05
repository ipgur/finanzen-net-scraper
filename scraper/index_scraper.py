import requests
from bs4 import BeautifulSoup

class IndexScraper:

    FINANZEN_NET_URL = "https://finanzen.net"

    def __init__(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        all_tables = soup.find_all("div", id="IndexShareListValues")
        self.aktien = []
        self.init(all_tables=all_tables)

    def init(self, all_tables):
        table = all_tables[0]

        all_a = table.find_all("a")
        for a in all_a:
            aktie = {"url": self.FINANZEN_NET_URL+a["href"], "title": a["title"]}
            self.aktien.append(aktie)

        print(self.aktien)

    def getAllAktien(self):
        return self.aktien

