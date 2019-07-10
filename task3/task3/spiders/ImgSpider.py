from scrapy.spiders import Spider

from ..items import ScrapyImgItem


class ImgSpider(Spider):
    name = "img_spider"
    start_urls = ["http://licenseplatemania.com/landenpaginas/zuidkorea.htm"]

    def parse(self, response):
        # 이미지 객체 준비
        item = ScrapyImgItem()
        img_urls = []
        # 부모가 body인 모든 a 태그 중 속성 중 ..으로 시작하는 태그 추출
        # https://www.w3schools.com/cssref/css_selectors.asp
        for img in response.css("body > a[href^=\"../\"]"):
            img_urls.append('http://licenseplatemania.com' + img.css("a::attr(href)").extract_first()[2:]) # 상대 경로 대신 절대 경로로 변환
        item["image_urls"] = img_urls
        return item
