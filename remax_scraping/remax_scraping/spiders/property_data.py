import scrapy
import logging
from scrapy import Request
import json
import numpy as np
from collections import Counter
from scrapy.crawler import CrawlerProcess


class Homes(scrapy.Spider):
    name = "rental_homes"

    def __init__(self, *args, **kwargs):
        self.myurls = kwargs.get('myurls', [])
        super(Homes, self).__init__(*args, **kwargs)

    def start_requests(self):
        for url in self.myurls:
            yield Request(url, self.parse)

    def parse(self, response):
        price = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "h3", " " ))]/text()').getall()[1].replace('\n', '').replace(' ', '')
        year_built = response.xpath('//div[contains(text(), "Year Built")]/following-sibling::div[1]/text()').get().replace('\n', '').replace(' ', '')


        yield {
            'price': price,
            'year_built': year_built
        }



