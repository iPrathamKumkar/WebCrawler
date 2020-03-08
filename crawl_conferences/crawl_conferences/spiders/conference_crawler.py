import scrapy
import time

class Scraper(scrapy.Spider):
    name  = "conference"
    page_number = 15
    start_urls = ["http://www.wikicfp.com/cfp/call?conference=big%20data%20&page=15"]

    def parse(self, response):
        Scraper.page_number += 1
        rows = response.xpath("//html//body//div[4]//center//form//table//tr[3]//td//table//tr")

        i = 1
        while i + 1 < len(rows):
            conference = dict()
            if len(rows[i].css("a::text")) > 0:
                conference['acronym'] = rows[i].css("a::text")[0].extract()
                conference['title'] = rows[i].css("td::text")[0].extract()
                conference['location']= rows[i + 1].css("td::text")[1].extract()
                i += 2
                yield conference
            else:
                i += 1
        time.sleep(7)
        next_page = "http://www.wikicfp.com/cfp/call?conference=big%20data%20&page=" + str(Scraper.page_number)
        if Scraper.page_number <= 20:
            yield response.follow(next_page, callback = self.parse)
