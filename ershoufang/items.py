# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#
# import scrapy
#
#
# class ErshoufangItem(scrapy.Item):
#     # define the fields for your item here like:
#     currentPage = scrapy.Field()
#
#     url = scrapy.Field()
#     title = scrapy.Field()
#     region = scrapy.Field()
#     houseInfo = scrapy.Field()
#     houseCode = scrapy.Field()
#     totalPrice = scrapy.Field()
#     publishDay = scrapy.Field()
#     visited = scrapy.Field()
#     attention = scrapy.Field()
#     unitPrice = scrapy.Field()
#
#     area = scrapy.Field()
#
#     # 房屋基本信息
#     houseNumType = scrapy.Field()
#     sourceId = scrapy.Field()
#     houseHeight = scrapy.Field()
#     houseBigSquare = scrapy.Field()
#     houseType = scrapy.Field()
#     houseInnerSquare = scrapy.Field()
#     houseStuctType = scrapy.Field()
#     houseDirctionType = scrapy.Field()
#     houseStuctMaterialType = scrapy.Field()
#     houseDecrateType = scrapy.Field()
#     houseIsWithLift = scrapy.Field()
#     houseRightYear = scrapy.Field()
#
#     # 房屋交易基本信息
#     tradeOnlineTime = scrapy.Field()
#     tradeRightType = scrapy.Field()
#     tradeLastTime = scrapy.Field()
#     tradeUseType = scrapy.Field()
#     tradeLostTime = scrapy.Field()
#     tradeHouseRightOwnType = scrapy.Field()
#     tradeGurantyMsg = scrapy.Field()
#     tradeHouseBookMsg = scrapy.Field()
#
#
#
#     pass
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class ErshoufangItem(Item):
    url = Field()
    title = Field()
    region = Field()
    houseInfo = Field()
    houseCode = Field()
    totalPrice = Field()
    publishDay = Field()
    visited = Field()
    attention = Field()
    unitPrice = Field()

    area = Field()

    # 房屋基本信息
    houseNumType = Field()
    sourceId = Field()
    houseHeight = Field()
    houseBigSquare = Field()
    houseType = Field()
    houseInnerSquare = Field()
    houseStuctType = Field()
    houseDirctionType = Field()
    houseStuctMaterialType = Field()
    houseDecrateType = Field()
    houseIsWithLift = Field()
    houseRightYear = Field()

    # 房屋交易基本信息
    tradeOnlineTime = Field()
    tradeRightType = Field()
    tradeLastTime = Field()
    tradeUseType = Field()
    tradeLostTime = Field()
    tradeHouseRightOwnType = Field()
    tradeGurantyMsg = Field()
    tradeHouseBookMsg = Field()

class ExampleLoader(ItemLoader):
    default_item_class = ErshoufangItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()