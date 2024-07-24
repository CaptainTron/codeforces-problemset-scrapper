# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CodeforcesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CodeforcesProblemSet(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    problem_rating = scrapy.Field()
    solved_by = scrapy.Field()
    tags = scrapy.Field()

