#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/1 21:20
# @Author  : Aries
# @Site    : 
# @File    : ershoufangnj.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import string

import scrapy
import re
import os
from ershoufang.conf.logControl import logControl

from scrapy import Selector

from ershoufang.items import ErshoufangItem
from scrapy_redis.spiders import RedisSpider



class ershoufangSpider(RedisSpider):
    name = "ershoufang"
    redis_key = 'myspider:start_urls'

    page = 1
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(ershoufangSpider, self).__init__(*args, **kwargs)
    def parse(self, response):
        # item = ErshoufangItem()
        # print("+================================wo get url:{url}".format(url=response.url))
        # houses = response.xpath(".//ul[@class='sellListContent']/li")
        # for house in houses:
        #     item.clear()
        #     try:
        #         attention = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[0]
        #         visited = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[1]
        #         if u'月' in house.xpath(".//div[@class='followInfo']/text()").extract()[0].split('/')[2]:
        #             number = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
        #             publishday = u'{days}'.format(days = int(number)*30)
        #         elif u'年' in house.xpath(".//div[@class='followInfo']/text()").extract()[0].split('/')[2]:
        #             publishday = '365'
        #         else:
        #             publishday = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
        #         url = house.xpath(".//a[@class='img ']/@href").extract()[0];
        #         self.logger.debug("------the url is {url}".format(url=url))
        #         # yield scrapy.Request(url, callback=self.parse_item)
        #         request = scrapy.Request(url, callback=self.parse_item)
        #         request.meta['item'] = item
        #         self.logger.info( item)
        #         print("------------------------------------------------------------------------------------------------end")
        #         yield item
        #         # self.item['url'] = response.url;
        #         # yield self.item
        #     except:
        #         print "These are some ecxeptions"
        #     else:
        #         pass
        # self.logger.info('****************fuck01******************')
        page = response.xpath("//div[@class='page-box house-lst-page-box'][@page-data]").xpath('@page-data').re("\d+")

        p = re.compile(r'.*ie[1-2]')
        self.logger.info('****************fuck02******************')
        self.logger.info('****************{page0}****{page1}****{small}**********'.format(page0=page[0],page1=page[1],small=min(int(page[0]),int(page[1]))))
        maxPage = max(int(page[0]),int(page[1]))
        urlList = []
        for pageNum in xrange(1,maxPage+1):
            aUrl = "{urlhead}/pg{urltail}".format(urlhead=p.match(response.url).group(),urltail=pageNum)
            urlList.append(aUrl)
            self.logger.info('****************wo have got nextPage:{aUrl}******************'.format(aUrl=aUrl))
            yield scrapy.http.Request(url = aUrl, callback=self.parsePages, dont_filter=True)
            self.logger.info('****************EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE**********')

    def parsePages(self, response):
        self.logger.info("#################################################################################parse_2 method running#################")
        houses = response.xpath(".//ul[@class='sellListContent']/li")
        for house in houses:
            aHouseDetailUrl = house.xpath(".//a[@class='img ']/@href").extract()[0];
            yield scrapy.http.Request(url = aHouseDetailUrl, callback=self.parseItem, dont_filter=True)
    def parseItem(self, response):
        item = ErshoufangItem()
        self.logger.info("#################################################################################parse_2 method running#################")
        area = response.xpath("//div[@class='areaName']/span[@class='info']/a[1]/text()").extract()[0];
        region = response.xpath("//div[@class='areaName']/span[@class='info']/a[2]/text()").extract()[0];
        title = response.xpath("//h1[@class='main']/text()").extract()[0];
        if "lianjia.com" in response.url:
            sourceId = 1;
        item['area'] = area;
        item['region'] = region;
        item['sourceId']=sourceId;
        item['title']=title;
        item['totalPrice'] = response.xpath("//span[@class='total']/text()").extract()[0];
        item['url'] = response.url;
        item['houseCode'] = response.xpath("//div[@class='houseRecord']/span[2]/text()").extract()[0];
        print item
# 房屋详细信息
        item['houseNumType'] = response.xpath("//div[@class='base']/div[@class='content']/ul/li[1]/text()").extract()[0];
        item['houseHeight'] = response.xpath("//div[@class='base']/div[@class='content']/ul/li[2]/text()").extract()[0];
        item['houseBigSquare'] = \
        response.xpath("//div[@class='base']/div[@class='content']/ul/li[3]/text()").extract()[0];
        item['houseType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[4]/text()").extract()[0];
        item['houseInnerSquare'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[5]/text()").extract()[0];
        item['houseStuctType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[6]/text()").extract()[0];
        item['houseDirctionType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[7]/text()").extract()[0];
        item['houseStuctMaterialType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[8]/text()").extract()[0];
        item['houseDecrateType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[9]/text()").extract()[0];
        item['houseIsWithLift'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[10]/text()").extract()[0];
        item['houseStuctType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[11]/text()").extract()[0];
        item['houseRightYear'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[12]/text()").extract()[0];
        item['unitPrice'] = response.xpath("//span[@class='unitPriceValue']/text()").extract()[0]
        item['attention'] = response.xpath("//span[@id='favCount']/text()").extract()[0];
        item['visited'] = response.xpath("//span[@id='cartCount']/text()").extract()[0];


        # 交易相关属性
        item['tradeOnlineTime'] = response.xpath("//div[@class='transaction']/div[@class='content']/ul/li[1]/span[2]/text()").extract()[0]
        item['tradeRightType'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[2]/span[2]/text()").extract()[0]
        item['tradeLastTime'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[3]/span[2]/text()").extract()[0]
        item['tradeUseType'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[4]/span[2]/text()").extract()[0]
        item['tradeLostTime'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[5]/span[2]/text()").extract()[0]
        item['tradeHouseRightOwnType'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[6]/span[2]/text()").extract()[0]
        item['tradeGurantyMsg'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[7]/span[2]/text()").extract()[0].lstrip().rstrip();
        item['tradeHouseBookMsg'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[8]/span[2]/text()").extract()[0]
        yield item
