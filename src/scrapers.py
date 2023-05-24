import datetime
from typing import Set, Union
from bs4 import BeautifulSoup

from src.metadata import BASE_URL
from src.utils import request_page, is_valid_news_url


class BaseScraper:

    def __init__(self, url: str):
        self.url = url

        html = request_page(url)
        self.soup = BeautifulSoup(html, "lxml")


class IndexPageScraper(BaseScraper):

    def get_news_urls(self) -> Set[str]:
        urls = set()
        for a_element in self.soup.find_all("a"):
            if a_element.get("href") is not None:

                url = a_element.get("href")
                if not url.startswith("http"):
                    url = BASE_URL + url

                if is_valid_news_url(url):
                    urls.add(url)
        return urls


class NewsPageScraper2003(BaseScraper):

    def get_title(self) -> str:

        if self.soup.find(name="span", class_="titulonoticia"):
            title_element = self.soup.find(name="span", class_="titulonoticia")
        else:
            return ""

        return title_element.text.strip() if title_element else ""

    def get_text(self) -> str:

        if self.soup.find(name="td", class_="trecepixnegro"):
            text_element = self.soup.find(name="td", class_="trecepixnegro")
        else:
            return ""

        text = "".join(element.text for element in text_element.find_all("p")[1:]).strip()
        return text


class NewsPageScraper2006(BaseScraper):

    def get_title(self) -> str:

        if self.soup.find(name="div", class_="noticia"):
            news_element = self.soup.find(name="div", class_="noticia")
        else:
            return ""

        if news_element.find(name="h1"):
            title_element = news_element.find(name="h1")
        elif news_element.find(name="h2"):
            title_element = news_element.find(name="h2")
        else:
            return ""

        return title_element.text.strip()

    def get_text(self) -> str:

        if self.soup.find(name="div", id="tamano"):
            text_element = self.soup.find(name="div", id="tamano")
        else:
            return ""

        text = "".join(element.text for element in text_element.find_all("p")).strip()
        return text


class NewsPageScraper2014(BaseScraper):

    def get_title(self) -> str:

        if self.soup.find(name="h1", itemprop="headline"):
            title_element = self.soup.find(name="h1", itemprop="headline")

        elif self.soup.find(name="h1"):
            title_element = self.soup.find(name="h1")
        else:
            return ""

        return title_element.text.strip()

    def get_text(self) -> str:

        if self.soup.find(name="div", itemprop="articleBody"):
            text_element = self.soup.find(name="div", itemprop="articleBody")
        elif self.soup.find(name="div", **{"data-section": "articleBody"}):
            text_element = self.soup.find(name="div", **{"data-section": "articleBody"})
        else:
            return ""

        text = "\n".join(element.text for element in text_element.find_all("p")).strip()
        return text


Scraper = Union[
    NewsPageScraper2003,
    NewsPageScraper2006,
    NewsPageScraper2014
]


def select_news_scrapper(date: datetime.date) -> Scraper:
    if date.year < 2006:
        return NewsPageScraper2003
    elif 2006 <= date.year < 2014:
        return NewsPageScraper2006
    else:
        return NewsPageScraper2014
