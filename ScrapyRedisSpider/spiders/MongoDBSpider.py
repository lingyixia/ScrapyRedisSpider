# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
import re, scrapy_redis.scheduler
import scrapy, scrapy_redis.queue
from ScrapyRedisSpider.items import ScrapyredisspiderItem


class MongodbspiderSpider(RedisSpider):
    name = 'MongoDBSpider'
    redis_key = 'MongoDBSpider:start_urls'
    allowed_domains = ['www.qidian.com']

    # start_urls = [
    #     'https://www.qidian.com/all?chanId=21&subCateId=8&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1']

    def parse(self, response):
        selector = Selector(response)
        item = ScrapyredisspiderItem()
        books = selector.xpath('''//div[@class='book-img-text']/ul/li/div[@class='book-mid-info']''')
        for book in books:
            item['bookName'] = book.xpath('''./h4/a/text()''').extract_first()
            item['bookAuthor'] = book.xpath('''./p[@class='author']/a[1]/text()''').extract_first()
            item['bootStyle'] = book.xpath('''./p[@class='author']/a[2]/text()''').extract_first()
            item['bookInfo'] = book.xpath('''./p[@class='intro']/text()''').extract_first()
            yield item
            nextUrl = selector.xpath('''//a[@class='lbf-pagination-next ']/@href''').extract_first()
            if nextUrl:
                nextUrl = 'https://' + nextUrl[2:]
                yield scrapy.Request(url=nextUrl, callback=self.parse)
