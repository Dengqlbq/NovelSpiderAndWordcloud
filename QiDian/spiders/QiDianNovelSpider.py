from QiDian.items import QiDianNovelItem
from scrapy.spider import Spider
from scrapy import Request


class QiDianNovelSpider(Spider):

    name = 'qi_dian_novel_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/53.0.2785.143 Safari/537.36'
    }
    page = 1
    url = 'http://f.qidian.com/all?chanId=21&orderId=&page=1&vip=\
                 hidden&style=1&pageSize=20&siteid=1&hiddenField=1&page=%d'

    def start_requests(self):
        yield Request(self.url % self.page, headers=self.header)

    def parse(self, response):

        item = QiDianNovelItem()
        novels = response.xpath('//ul[@class="all-img-list cf"]/li/div[@class="book-mid-info"]')

        for novel in novels:
            item['name'] = novel.xpath('.//h4/a/text()').extract()[0]
            item['author'] = novel.xpath('.//p[@class="author"]/a[1]/text()').extract()[0]
            item['intro'] = novel.xpath('.//p[@class="intro"]/text()').extract()[0]

            yield item
            if self.page < 20:
                self.page += 1
                yield Request(self.url % self.page, headers=self.header)
