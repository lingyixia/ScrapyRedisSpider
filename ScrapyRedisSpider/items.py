# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyredisspiderItem(scrapy.Item):
    bookName = scrapy.Field()
    bookAuthor = scrapy.Field()
    bootStyle = scrapy.Field()
    bookInfo = scrapy.Field()
