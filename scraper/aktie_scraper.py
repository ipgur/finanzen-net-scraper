import requests
from bs4 import BeautifulSoup

class AktieScraper:
    def __init__(self, url):

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        all_tables = soup.find_all("div", class_="box table-quotes")
        self.kurs_matrix = []
        self.init(all_tables=all_tables)

    def init(self, all_tables):
        for table in all_tables:
            if "Daten im Zeitverlauf" in str(table):
                thead = table.find_all("th")
                keys = []
                for i in range(len(thead)):
                    keys.append(str(thead[i]).strip("<th class=\"\">").strip("</th>").strip("<th>"))

                tbody = table.find_all("td")
                data = {}
                for i in range(len(tbody)):
                    if i % len(thead) == 0:
                        data = {}

                    data[keys[i % len(thead)]] = str(tbody[i]).strip("</td>").strip("<td>").replace(",", ".")

                    if i % len(thead) == len(thead) - 1:
                        self.kurs_matrix.append(data)

    def min_last_5(self):
        for entry in self.kurs_matrix:
            if entry["Datum"] == "5 Jahre":
                return entry["Tief"]

    def max_last_5(self):
        for entry in self.kurs_matrix:
            if entry["Datum"] == "5 Jahre":
                return entry["Hoc"]

    def max_today(self):
        for entry in self.kurs_matrix:
            if entry["Datum"] == "Heute":
                return entry["Hoc"]

    def min_today(self):
        for entry in self.kurs_matrix:
            if entry["Datum"] == "Heute":
                return entry["Tief"]

    def schluss_kurs(self):
        for entry in self.kurs_matrix:
            if entry["Datum"] == "Heute":
                return entry["Schlusskurs"]