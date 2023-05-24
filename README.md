# ElMundo News Scraper

This tool allows for the efficient extraction of news articles from the [ElMundo news library](https://www.elmundo.es/elmundo/hemeroteca). ElMundo's library maintains a repository of news articles dating back to 2003. The scraper navigates morning, afternoon, and evening index pages for each day, harvesting all news URLs. Subsequently, it accesses each news page and extracts the relevant content.

## Output Data

The scraper stores the following attributes for each article:

- `source`: The source of the news, preset to "ElMundo".
- `title`: The title derived from the news page.
- `url`: The URL from which the news article was extracted.
- `dct`: Document Creation Time, denoting the date of the news article creation in the format `YYYY-MM-DD`.
- `text`: The full text extracted from the news page.

The scraped data is collated into a `.csv` file, which is stored in the `data/` directory at the root of the current project directory.

## Setup & Usage Instructions

Below are the steps to set up your environment and run the scraper on your machine.

### Environment Setup

1. Create and activate a Python virtual environment.

```shell
virtualenv venv --python=python3.8
source venv/bin/activate
```

2. Install the project dependencies.

```shell
pip install -r requirements.txt
```

### Scraping Data

To scrape news articles for a specific date range, use the following command:

```shell
python -m src.scrape --start_date "2004-01-01" --end_date "2004-12-31" --output_file "news04.csv"
```

This command collects news articles from the year 2004 and stores them in the `data/news04.csv` file. Regarding runtime, expect approximately an hour for each year you intend to scrape. The resulting file size is estimated to be around 40 MB per year.
