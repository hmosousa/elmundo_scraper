import csv
import datetime
import logging.config
from pathlib import Path
from typing import List, Dict

from src.cli import setup_parser
from src.metadata import MOMENTS, FIRST_RECORD, LIBRARY_URL
from src.scrapers import IndexPageScraper, select_news_scrapper
from src.utils import date_from_news_url

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True)

LOGS_PATH = Path("logs")
LOGS_PATH.mkdir(exist_ok=True)

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


def scrape_one_day(date: datetime.date) -> List[Dict]:
    """Scrape ElMundo index page on a specific date. The extraction returns
    a list of news that where published in that specific date."""

    if date < FIRST_RECORD:
        msg = f"The provided date is out of bounds. " \
              f"Please provide a date between {FIRST_RECORD.strftime('%Y-%m-%d')} " \
              f"and {datetime.date.today().strftime('%Y-%m-%d')}."
        raise ValueError(msg)

    news_urls = set()
    for moment in MOMENTS:
        index_url = f"{LIBRARY_URL}/{date.year}/{date.month:02}/{date.day:02}/{moment}/index.html"

        try:
            index_scraper = IndexPageScraper(index_url)
        except:
            logger.warning(f"There was a problem scraping url {index_url}."
                           f"Proceeding for the following url.")
            continue
        moment_news_urls = index_scraper.get_news_urls()
        news_urls.update(moment_news_urls)

    NewsPageScraper = select_news_scrapper(date)
    news = []
    for news_url in news_urls:
        news_date = date_from_news_url(news_url)
        if news_date == date:  # index page might contain references to previous days' news.

            logger.info(f"Extracting news from url {news_url}.")

            try:
                news_scraper = NewsPageScraper(news_url)
            except:
                logger.warning(f"There was a problem scraping url {news_url}."
                               f"Proceeding for the following url.")
                continue

            title = news_scraper.get_title()
            text = news_scraper.get_text()

            if title == "" or text == "":
                continue

            logger.info(f"Extracted the news with:\n\tTitle: \'{title}\'\n")
            logger.debug(f"\tText: \'{text[:50]}\'")

            news.append({
                "source": "El Mundo",
                "title": title,
                "url": news_url,
                "dct": date.strftime("%Y-%m-%d"),
                "text": text
            })

    return news


def main() -> None:
    parser = setup_parser()
    args = parser.parse_args()

    start_date = datetime.date.fromisoformat(args.start_date)
    end_date = datetime.date.fromisoformat(args.end_date)

    if start_date > end_date:
        logger.error("Start date must be lower than the end date.")
        return

    with open(DATA_PATH / args.output_file, "w", encoding="utf-8") as fout:
        fieldnames = ["source", "title", "url", "dct", "text"]
        writer = csv.DictWriter(
            fout,
            delimiter=",",
            quotechar="\"",
            quoting=csv.QUOTE_NONNUMERIC,
            fieldnames=fieldnames
        )

        writer.writeheader()

        delta = end_date - start_date
        dates = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
        for date in dates:
            logger.info(f"Scraping ElMundo from date {date.strftime('%Y-%m-%d')}")
            date_news = scrape_one_day(date)
            for news in date_news:
                writer.writerow(news)


if __name__ == "__main__":
    main()
