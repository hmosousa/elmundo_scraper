import datetime

from src.utils import (
    is_valid_news_url,
    date_from_news_url
)


def test_is_valid_news_url_base():
    url = "https://www.elmundo.es/elmundo/2010/01/01/espana/1262340352.html"
    result = is_valid_news_url(url)
    expected_result = True
    assert result == expected_result


def test_is_valid_news_url_end_of_url():
    url = "https://www.elmundo.es/elmundo/2010/01/01/espana/1262340352.html#comentarios"
    result = is_valid_news_url(url)
    expected_result = False
    assert result == expected_result


def test_is_valid_news_url_new_url_2014():
    """In 2014 the news url structure was changed."""

    url = "https://www.elmundo.es/espana/2014/01/01/52c3c24a268e3ec5218b456b.html"
    result = is_valid_news_url(url)
    expected_result = True
    assert result == expected_result


def test_date_from_news_url():
    url = "https://www.elmundo.es/elmundo/2010/01/01/espana/1262340352.html"
    result = date_from_news_url(url)
    expected_result = datetime.date(year=2010, month=1, day=1)
    assert result == expected_result
