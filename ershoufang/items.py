# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    region = scrapy.Field()
    houseInfo = scrapy.Field()
    houseCode = scrapy.Field()
    totalPrice = scrapy.Field()
    publishDay = scrapy.Field()
    visited = scrapy.Field()
    attention = scrapy.Field()
    unitPrice = scrapy.Field()
    # recordTime = scrapy.Field()
    area = scrapy.Field()

    # 房屋基本信息
    houseNumType = scrapy.Field()
    sourceId = scrapy.Field()
    houseHeight = scrapy.Field()
    houseBigSquare = scrapy.Field()
    houseType = scrapy.Field()
    houseInnerSquare = scrapy.Field()
    houseStuctType = scrapy.Field()
    houseDirctionType = scrapy.Field()
    houseStuctMaterialType = scrapy.Field()
    houseDecrateType = scrapy.Field()
    houseIsWithLift = scrapy.Field()
    houseRightYear = scrapy.Field()

    # 房屋交易基本信息
    tradeOnlineTime = scrapy.Field()
    tradeRightType = scrapy.Field()
    tradeLastTime = scrapy.Field()
    tradeUseType = scrapy.Field()
    tradeLostTime = scrapy.Field()
    tradeHouseRightOwnType = scrapy.Field()
    tradeGurantyMsg = scrapy.Field()
    tradeHouseBookMsg = scrapy.Field()



    pass
