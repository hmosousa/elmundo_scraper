import datetime
import logging
import re

import requests

logger = logging.getLogger(__name__)


def is_valid_news_url(url: str) -> bool:
    """Check if an url follows the structure of a valid news url."""
    match = re.match(r"https://www.elmundo.es/\w+/\d{4}/\d{2}/\d{2}/\w*/*\w+.html$", url)
    return match is not None


def request_page(url: str) -> str:
    """Request url page. It will return the html text of the url."""
    response = requests.get(url)
    if not response.ok:
        logger.warning(f"Response to request of page {url} came with code {response.status_code}.")
        return ""
    return response.text


def date_from_news_url(url: str) -> datetime.date:
    """Each news url has the date of the news embedded in the url.
    For example https://www.elmundo.es/elmundo/2004/01/01/madrid/1072959605.html
    This function extract the date from the url."""
    [(year, month, day)] = re.findall(r"(\d{4})/(\d{2})/(\d{2})", url)
    year, month, day = int(year), int(month), int(day)
    return datetime.date(year=year, month=month, day=day)
