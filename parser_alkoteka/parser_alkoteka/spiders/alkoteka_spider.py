import scrapy


class AlkotekaSpiderSpider(scrapy.Spider):
    name = "alkoteka_spider"
    allowed_domains = ["alkoteka.com"]
    start_urls = ["https://alkoteka.com"]

    def parse(self, response):
        pass
