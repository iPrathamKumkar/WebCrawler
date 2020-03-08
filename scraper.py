import scrapy
import collections

class Scraper(scrapy.Spider):
    name  = "conference_spider"
    start_urls = ["http://www.wikicfp.com/cfp/call?conference=big%20data%20&page=1"]

    def parse(self, response):
        rows = response.xpath("//html//body//div[4]//center//form//table//tr[3]//td//table//tr")

        i = 1
        j = 2
        while j < len(rows):
            conference = dict()
            conference['acronym'] = rows[i].css("a::text")[0].extract()
            conference['title'] = rows[i].css("td::text")[0].extract()
            conference['location']= rows[j].css("td::text")[1].extract()
            i += 2
            j += 2
            yield conference
