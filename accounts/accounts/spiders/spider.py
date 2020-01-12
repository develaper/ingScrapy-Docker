# -*- coding: utf-8 -*-
import scrapy
import json


class SpiderSpider(scrapy.Spider):
#class SpiderSpider(scrapy):
    name = 'spider'
    allowed_domains = ['ing.ingdirect.es']
    #start_urls = ['https://ing.ingdirect.es/genoma_login/rest/session']

    def start_requests(self):
        headers = {
          'Accept':'*/*',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
          'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
          'Host': 'ing.ingdirect.es',
          'Content-Type':'application/json; charset=UTF-8',
          'Origin': 'https://ing.ingdirect.es',
          'Referer': 'https://ing.ingdirect.es/app-login/',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-origin',
          'X-Requested-With': 'XMLHttpRequest',
        }
        meta = {
            'handle_httpstatus_all': True
            }
        params = {
            "birthday":"01/07/1970",
            "device":"desktop",
            "loginDocument":{"document":"33333333B","documentType":0}
        }

        print(json.dumps(params))

        yield scrapy.Request(
            url='https://ing.ingdirect.es/genoma_login/rest/session',
            callback=self.parse,
            method='POST',
            body=json.dumps(params),
            headers=headers,
            meta=meta
        )


    def parse(self, response):
        #pass
        print(response.status)
        print(response.body)

        yield { "foo": "bar" }
