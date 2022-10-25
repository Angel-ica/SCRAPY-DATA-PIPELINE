# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespace(value):
    return value.strip()

# 
# class WebcrawlItem(scrapy.Item):
#     # define the fields for your item here like:
#     name = scrapy.Field()
#     price = scrapy.Field()
#     url = scrapy.Field()
class webcrawlItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace,'\n'),output_processor=TakeFirst(), )
    price = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace,'\n'),output_processor=TakeFirst(), )
    url = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace,'\n'),output_processor=TakeFirst(), )
