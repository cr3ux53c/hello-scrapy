import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # print(response.xpath("//title/text()").extract())
        # print()
        # print(response.xpath("//span[@class='text']/text()").extract())
        # print()
        # print(response.xpath("//span[@class='text']/text()")[1].extract())
        # print()
        # print(response.css('li.next a').xpath('@href').extract())
        # print()
        # print(response.css('a').xpath('@href').extract())

        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
