# -*- coding: utf-8 -*-
import scrapy
import re
import logging
LOG_FILENAME = '/Volumes/Mac/projects/pycharmProjects/ershoufang/logging_example.out'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,)
from scrapy import Selector

from ershoufang.items import ErshoufangItem


class ershoufangSpider(scrapy.Spider):
    name = "ershoufang"
    # start_urls = ["http://bj.lianjia.com/ershoufang/dongcheng/pg1", "http://bj.lianjia.com/ershoufang/xicheng/pg1", "http://bj.lianjia.com/ershoufang/chaoyang/pg1", "http://bj.lianjia.com/ershoufang/haidian/pg1", "http://bj.lianjia.com/ershoufang/fengtai/pg1", "http://bj.lianjia.com/ershoufang/shijingshan/pg1", "http://bj.lianjia.com/ershoufang/tongzhou/pg1", "http://bj.lianjia.com/ershoufang/changping/pg1", "http://bj.lianjia.com/ershoufang/daxing/pg1", "http://bj.lianjia.com/ershoufang/yizhuangkaifaqu/pg1", "http://bj.lianjia.com/ershoufang/shunyi/pg1", "http://bj.lianjia.com/ershoufang/fangshan/pg1", "http://bj.lianjia.com/ershoufang/mentougou/pg1", "http://bj.lianjia.com/ershoufang/pinggu/pg1", "http://bj.lianjia.com/ershoufang/huairou/pg1", "http://bj.lianjia.com/ershoufang/miyun/pg1", "http://bj.lianjia.com/ershoufang/yanqing/pg1", "http://bj.lianjia.com/ershoufang/yanjiao/pg1"]
    start_urls = ["http://nj.lianjia.com/ershoufang/pg1"]
    item = ErshoufangItem()
    def parse(self, response):
        houses = response.xpath(".//ul[@class='sellListContent']/li")
        for house in houses:
            self.item.clear()
            attention = ''
            visited = ''
            publishday = ''
            try:
                attention = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[0]
                visited = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[1]
                if u'月' in house.xpath(".//div[@class='followInfo']/text()").extract()[0].split('/')[2]:
                    number = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
                    publishday = u'{days}'.format(days = int(number)*30)

                elif u'年' in house.xpath(".//div[@class='followInfo']/text()").extract()[0].split('/')[2]:
                    # number = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
                    publishday = '365'
                else:
                    publishday = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[2]
                url = house.xpath(".//a[@class='img ']/@href").extract();
                print("------the url is {url}".format(url=url))
                # self.item['region'] = house.xpath(".//div[@class='houseInfo']/a/text()").extract();
                # self.item['url'] = house.xpath(".//a[@class='img ']/@href").extract();
                # self.item['houseInfo'] = house.xpath(".//div[@class='houseInfo']/text()").extract()
                # self.item['houseCode'] = house.xpath(".//a[@class='img ']/@data-housecode").extract()
                # self.item['unitPrice'] = house.xpath(".//div[@class='unitPrice']/span").re("\d+.\d+")
                # self.item['attention'] = attention;
                # self.item['visited'] = visited;
                #
                # self.item['publishDay'] = publishday;
                yield scrapy.Request(url[0], callback=self.parse_item)

            except:
                logging.exception('Got exception on main handler')
                print "These are some ecxeptions"
            else:
                pass

            # self.item = self.item + {
            #     'region': house.xpath(".//div[@class='houseInfo']/a/text()").extract(),
            #     'url':house.xpath(".//a[@class='img ']/@href").extract(),
            #     'houseInfo':house.xpath(".//div[@class='houseInfo']/text()").extract(),
            #     'houseCode':house.xpath(".//a[@class='img ']/@data-housecode").extract(),
            #     'unitPrice':house.xpath(".//div[@class='unitPrice']/span").re("\d+.\d+"),
            #     'totalPrice':house.xpath(".//div[@class='totalPrice']/span").re("\d+.\d+"),
            #     'attention': attention,
            #     'visited': visited,
            #     'publishDay': publishday,
            #
            # };


        page = response.xpath("//div[@class='page-box house-lst-page-box'][@page-data]").re("\d+")
        p = re.compile(r'[^\d]+')
        if len(page)>1 and page[0] != page[1]:
            next_page = p.match(response.url).group()+str(int(page[1])+1)
            print next_page+"*********************"
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_item(self, response):
        area = response.xpath("//div[@class='areaName']/span[@class='info']/a[1]/text()").extract()[0];
        title = response.xpath("//h1[@class='main']/text()").extract()[0];
        if "lianjia.com" in response.url:
            sourceId = 1;
        self.item['area'] = area;
        self.item['sourceId']=sourceId;
        self.item['title']=title;
        self.item['region'] = response.xpath("//span[@class='total']/text()").extract()[0];
        self.item['url'] = response.url;
        self.item['houseNumType'] = response.xpath("//div[@class='base']/div[@class='content']/ul/li[1]/text()").extract()[0];
        self.item['houseHeight'] = response.xpath("//div[@class='base']/div[@class='content']/ul/li[2]/text()").extract()[0];
        self.item['houseBigSquare'] = \
        response.xpath("//div[@class='base']/div[@class='content']/ul/li[3]/text()").extract()[0];
        self.item['houseType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[4]/text()").extract()[0];
        self.item['houseInnerSquare'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[5]/text()").extract()[0];
        self.item['houseStuctType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[6]/text()").extract()[0];
        self.item['houseDirctionType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[7]/text()").extract()[0];
        self.item['houseStuctMaterialType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[8]/text()").extract()[0];
        self.item['houseDecrateType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[9]/text()").extract()[0];
        self.item['houseIsWithLift'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[10]/text()").extract()[0];
        self.item['houseStuctType'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[11]/text()").extract()[0];
        self.item['houseRightYear'] = \
            response.xpath("//div[@class='base']/div[@class='content']/ul/li[12]/text()").extract()[0];
        self.item['unitPrice'] = response.xpath("//span[@class='unitPriceValue']/text()").extract()[0]
        self.item['attention'] = response.xpath("//span[@id='favCount']/text()").extract()[0];
        self.item['visited'] = response.xpath("//span[@id='cartCount']/text()").extract()[0];


        # 交易相关属性
        self.item['tradeOnlineTime'] = response.xpath("//div[@class='transaction']/div[@class='content']/ul/li[1]/span[2]/text()").extract()[0]
        self.item['tradeRightType'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[2]/span[2]/text()").extract()[0]
        self.item['tradeLastTime'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[3]/span[2]/text()").extract()[0]
        self.item['tradeUseType'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[4]/span[2]/text()").extract()[0]
        self.item['tradeLostTime'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[5]/span[2]/text()").extract()[0]
        self.item['tradeHouseRightOwnType'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[6]/span[2]/text()").extract()[0]
        self.item['tradeGurantyMsg'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[7]/span[2]/text()").extract()[0]
        self.item['tradeHouseBookMsg'] = response.xpath(
            "//div[@class='transaction']/div[@class='content']/ul/li[8]/span[2]/text()").extract()[0]


        print("---------this is item now:{item}".format(item=self.item))
        # yield self.item
        self.item.clear()
