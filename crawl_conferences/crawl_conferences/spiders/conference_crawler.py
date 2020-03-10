# Import the required libraries
import scrapy
import time


class Scraper(scrapy.Spider):
    # Naming the spider
    name  = "conferences"
    # Initial page number to start crawling from
    page_number = 1

    # The URL where the crawling should begin from
    start_urls = ["http://www.wikicfp.com/cfp/call?conference=artificial%20intelligence&page=1"]

    # Function used by scrapy for the crawling operation
    def parse(self, response):
        # Increment the page number for moving to the next page
        Scraper.page_number += 1

        # Xpath for reaching the required tag within the HTML for extracting data
        rows = response.xpath("//html//body//div[4]//center//form//table//tr[3]//td//table//tr")

        i = 1
        while i + 1 < len(rows):
            # scrapy accepts dictionary as an output
            conference = dict()

            # Only extract data if a conference link is present in the row
            if len(rows[i].css("a::text")) > 0:
                # Extract the acronym, title, and location using appropriate CSS selectors
                conference['acronym'] = rows[i].css("a::text")[0].extract()
                conference['title'] = rows[i].css("td::text")[0].extract()
                conference['location']= rows[i + 1].css("td::text")[1].extract()
                i += 2
                # Output the scraped data
                yield conference
            else:
                i += 1

        # URL for the next page
        next_page = "http://www.wikicfp.com/cfp/call?conference=artificial%20intelligence&page=" + str(Scraper.page_number)

        # Limiting the crawl to 20 pages
        if Scraper.page_number <= 20:
            yield response.follow(next_page, callback = self.parse)
