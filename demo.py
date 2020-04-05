from scraper.aktie_scraper import AktieScraper
from scraper.index_scraper import IndexScraper


def main():
    # define index
    index_scraper = IndexScraper("https://www.finanzen.net/index/mdax")
    # scrape it and get all aktien
    all_aktien = index_scraper.getAllAktien()

    # scrape each one of them to extract statistic
    for aktie in all_aktien:
        scrape = AktieScraper(aktie["url"])
        print(aktie["title"] + "\t" + aktie["url"] + "\t" + str(scrape.schluss_kurs() + "\t" + str(scrape.min_last_5())
                                                                + "\t" + str(scrape.max_last_5()) + "\t"))


if __name__ == "__main__":
    main()
