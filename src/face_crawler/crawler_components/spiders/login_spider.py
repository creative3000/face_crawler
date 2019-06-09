import scrapy
from scrapy import FormRequest, Spider
from scrapy.conf import settings


class LoginSpider(Spider):
    name = 'login'

    def start_requests(self):
        yield scrapy.Request('https://www.facebook.com/login', self.parse, dont_filter=True)

    def parse(self, response):
        yield FormRequest.from_response(response, formdata=settings['CREDENTIALS'],
                                        callback=self.after_login, dont_filter=True)

    def after_login(self, response):
        # if not 200 you should stop crawling
        if response.status == 200:
            print("LOGGED IN SUCCESFULLY")
        else:
            print("INVALID CREDENTIALS")
            # shut down somehow
