# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['ing.ingdirect.es']
    start_urls = ['https://ing.ingdirect.es/app-login/']

    def parse(self, response):
        print("response")
        print(response)
