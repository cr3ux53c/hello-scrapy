from scrapy.spiders import Spider

from ..items import ScrapyImgItem


class ImgSpider(Spider):
    name = "img_spider"
    start_urls = ["http://licenseplatemania.com/landenpaginas/zuidkorea.htm"]

    def parse(self, response):
        # 이미지 객체 준비
        item = ScrapyImgItem()
        img_urls = []
        # 응답 HTML의 thumbs_list_frame id를 가진 요소가 부모인 모든 li 태그를 추출
        for img in response.css("body a"):
            # a 태그의 href 속성값을 추출해서 img_urls에 추가
            img_urls.append(img.css("a::attr(href)").extract_first())
        item["image_urls"] = img_urls
        return item
