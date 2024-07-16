# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrappingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# adding items from the 'yield' of sigmaSipider's 'book'
class BookItem(scrapy.Item):

    URL = scrapy.Field()
    TITLE = scrapy.Field()
    PRODUCTTYPE = scrapy.Field()
    PRICE_INCL_TAX = scrapy.Field()
    TAX = scrapy.Field()
    AVAILABILITY = scrapy.Field()
    REVIEW = scrapy.Field()
    STARS = scrapy.Field()
    CATEGORIES = scrapy.Field()
    DESCRIPTION = scrapy.Field()
