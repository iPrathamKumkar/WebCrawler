# WebCrawler

A simple web crawler for scraping data.

## Using the crawler

Clone the repository:

```
git clone https://github.com/iPrathamKumkar/Real-Estate-Price-Prediction-Flask.git
```

Install the pre-requisite libraries:

```
pip install requirements.txt
```

Edit the start_urls and the next_page fields to meet your requirements:

```
start_urls = ["http://www.wikicfp.com/cfp/call?conference=artificial%20intelligence&page=1"]
next_page = "http://www.wikicfp.com/cfp/call?conference=artificial%20intelligence&page=" + str(Scraper.page_number)
```

## Built With

* [Scrapy](https://docs.scrapy.org/en/latest/) - The framework used for extracting data

## Authors

* **Prathamesh Kumkar** - [iPrathamKumkar](https://github.com/iPrathamKumkar)
