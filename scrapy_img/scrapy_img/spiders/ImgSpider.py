from scrapy.spiders import Spider

from ..items import ScrapyImgItem


class ImgSpider(Spider):
    name = "img_spider"
    start_urls = ["http://automationpractice.com/index.php?id_product=2&controller=product"]

    def parse(self, response):
        item = ScrapyImgItem()
        img_urls = []
        for img in response.css("#thumb_list_frame > li"):
            img_urls.append(img.css("a::attr(href)").extract_first())
        item["image_urls"] = img_urls
        return item
