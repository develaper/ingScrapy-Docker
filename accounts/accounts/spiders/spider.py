# -*- coding: utf-8 -*-
import scrapy
import json


class SpiderSpider(scrapy.Spider):
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

        yield scrapy.Request(
            url='https://ing.ingdirect.es/genoma_login/rest/session',
            callback=self.requestPinPad,
            method='POST',
            body=json.dumps(params),
            headers=headers,
            meta=meta
        )

    def requestPinPad(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        responsePinPositions = jsonresponse["pinPositions"]
        processId = jsonresponse["processId"]
        pinPadNumbers = jsonresponse["pinPadNumbers"]
        secretPin = ["1","2","3","4","5","6"]
        pinPositions = []
        for x in responsePinPositions:
            pinPositions.append(pinPadNumbers.index(int(secretPin[x-1])))
            #raise error if not in list although it should not happen it could happen

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
          'Connection': 'keep-alive',
        }
        meta = {
            'handle_httpstatus_all': True
        }
        params = {
            "pinPositions": pinPositions,
            "processId": processId
        }

        yield scrapy.Request(
            url='https://ing.ingdirect.es/genoma_login/rest/session',
            callback=self.requestTicket,
            method='PUT',
            body=json.dumps(params),
            headers=headers,
            meta=meta
        )

    def requestTicket(self, response):
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

        jsonresponse = json.loads(response.body_as_unicode())
        responseTicket = jsonresponse["ticket"]

        params = {
            "ticket":responseTicket,
            "device":"desktop"
        }

        yield scrapy.FormRequest(
            url='https://ing.ingdirect.es/genoma_api/login/auth/response',
            callback=self.requestClient,
            method='POST',
            formdata=json.dumps(params),
            headers=headers,
            meta=meta
        )

    def requestClient(self, response):
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

        yield scrapy.Request(
            url='https://ing.ingdirect.es/genoma_api/rest/client',
            callback=self.requestFpm,
            method='GET',
            headers=headers,
            meta=meta
        )

    def requestFpm(self, response):
        pass
