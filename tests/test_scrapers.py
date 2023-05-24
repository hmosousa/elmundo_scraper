from src.scrapers import (
    NewsPageScraper2003,
    NewsPageScraper2006,
    NewsPageScraper2014
)


class TestNewsPageScraper2003:

    def test_base(self):
        url = "https://www.elmundo.es/elmundo/2003/01/01/sociedad/1041411079.html"
        scraper = NewsPageScraper2003(url)

        title = scraper.get_title()
        expected_title = "Garzón, Bisbal, Aznar... los más relevantes de 2002"
        assert title == expected_title

        text = scraper.get_text()
        expected_text = "MADRID.- \n\nLos lectores de elmundo.es han"
        assert text.startswith(expected_text)

    def test_missing_title(self):
        url = "https://www.elmundo.es/elmundo/2005/01/01/descodificador/1104564030.html"
        scraper = NewsPageScraper2003(url)

        title = scraper.get_title()
        expected_title = ""
        assert title == expected_title

        text = scraper.get_text()
        expected_text = "El éxito de audiencia estaba garantizado"
        assert text.startswith(expected_text)


class TestNewsPageScraper2006:

    def test_base(self):
        url = "https://www.elmundo.es/elmundo/2006/01/01/sociedad/1136145198.html"
        scraper = NewsPageScraper2006(url)

        title = scraper.get_title()
        expected_title = "Muere una mujer en Granada tras ser disparada por su ex marido"
        assert title == expected_title

        text = scraper.get_text()
        expected_text = "GRANADA.- Pilar Pacheco Valverde"
        assert text.startswith(expected_text)

    def test_image_url(self):
        url = "https://www.elmundo.es/albumes/2007/01/01/emergencias/index.html"
        scraper = NewsPageScraper2006(url)

        title = scraper.get_title()
        expected_title = ""
        assert title == expected_title

        text = scraper.get_text()
        expected_text = ""
        assert text.startswith(expected_text)

    def test_video_url(self):
        url = "https://www.elmundo.es/elmundo/2009/01/01/videos/1230809278.html"
        scraper = NewsPageScraper2006(url)

        title = scraper.get_title()
        expected_title = ""
        assert title == expected_title

        text = scraper.get_text()
        expected_text = ""
        assert text.startswith(expected_text)

    def test_news_with_video(self):
        url = "https://www.elmundo.es/elmundo/2010/01/01/espana/1262343320.html"
        scraper = NewsPageScraper2006(url)

        title = scraper.get_title()
        expected_title = "Zapatero centra la Presidencia 'en la lucha por la superación de la crisis'"
        assert title == expected_title

        text = scraper.get_text()
        expected_text = "El presidente del Gobierno"
        assert text.startswith(expected_text)


class TestNewsPageScraper2014:

    def test_base(self):
        url = "https://www.elmundo.es/economia/2014/01/01/52c30e6222601db57e8b4579.html"
        scraper = NewsPageScraper2014(url)

        title = scraper.get_title()
        expected_title = "Fondos de EEUU y de Australia quieren comprar las autopistas en quiebra"
        assert title == expected_title

        text = scraper.get_text()
        expected_text = "No sólo los inmuebles tóxicos tienen"
        assert text.startswith(expected_text)

    def test_2016_news(self):
        url = "https://www.elmundo.es/cultura/2016/01/01/5686b7e222601df1408b458e.html"
        scraper = NewsPageScraper2014(url)

        title = scraper.get_title()
        expected_title = "Muere la inolvidable Natalie Cole"
        assert title == expected_title

        text = scraper.get_text()
        expected_text = "La hija de Nat \'King\' Cole"
        assert text.startswith(expected_text)

    def test_2017_news(self):
        url = "https://www.elmundo.es/internacional/2017/01/01/5868bae4268e3e384b8b45b8.html"
        scraper = NewsPageScraper2014(url)

        title = scraper.get_title()
        expected_title = "Las víctimas del club Reina: \"Algunas personas pisoteaban a otras. No sé cómo logré huir\""
        assert title == expected_title

        text = scraper.get_text()
        expected_text = "Grita, dice que tiene que pasar"
        assert text.startswith(expected_text)
