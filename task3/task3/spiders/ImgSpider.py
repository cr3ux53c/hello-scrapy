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
        for img in response.css("body > a[href^=\"../\"]"):  # css selector로 body의 a href="../"로 시작하는 태그들만 검색
            imgurl = img.css("a::attr(href)").extract_first()
            imgurl = "http://licenseplatemania.com" + imgurl[2:]  # 페이지에 ../~~ 의 상대 주소로 적혀있기때문에 필요없는부분 잘라내고 절대적 주소로 변경
            print(imgurl)
            img_urls.append(imgurl)
        item["image_urls"] = img_urls
        return item
