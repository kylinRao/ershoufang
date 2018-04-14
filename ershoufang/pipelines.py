# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3

from datetime import datetime
from conf.logControl import logControl
from db.dbInit import conn


class ErshoufangPipeline(object):
    logger = logControl.getLogger()
    DATABASE = os.path.join(os.path.dirname(__file__), 'ershoufang.db')

    def process_item(self, item, spider):
        self.logger.info("#############process_item start###############")

        sqlHouseBaseInfo = u"replace into houseBaseInfo (houseCode,url,visited,region,area,attention,sourceId) values ('{houseCode}','{url}','{visited}','{region}','{area}','{attention}','{sourceId}')";
        sqlHouseEveryDayPrice = u"replace into houseEveryDayPrice (houseCode,date,totalPrice,unitPrice,updateTime) values ('{houseCode}','{date}','{totalPrice}','{unitPrice}','{updateTime}')";
        sqlHouseDetailInfo = u"replace into houseDetailInfo (houseId,date,houseNumType,houseHeight,houseBigSquare,houseInnerSquare,houseStuctType,houseDirctionType,houseStuctMaterialType,houseDecrateType,houseIsWithLift,houseRightYear,tradeOnlineTime,tradeRightType,tradeLastTime,tradeUseType,tradeLostTime,tradeHouseRightOwnType,tradeGurantyMsg,tradeHouseBookMsg) values ('{houseId}','{date}','{houseNumType}','{houseHeight}','{houseBigSquare}','{houseInnerSquare}','{houseStuctType}','{houseDirctionType}','{houseStuctMaterialType}','{houseDecrateType}','{houseIsWithLift}','{houseRightYear}','{tradeOnlineTime}','{tradeRightType}','{tradeLastTime}','{tradeUseType}','{tradeLostTime}','{tradeHouseRightOwnType}','{tradeGurantyMsg}','{tradeHouseBookMsg}')"
        sqlHouseBaseInfoF = sqlHouseBaseInfo.format(houseCode=item['houseCode'],

                                                    url=item['url'],
                                                    visited=item['visited'],
                                                    region=item['region'],
                                                    area=item['area'],
                                                    attention=item['attention'],
                                                    sourceId=item['sourceId']
                                                    )
        sqlHouseEveryDayPriceF = sqlHouseEveryDayPrice.format(houseCode=item['houseCode'],
                                                              date=datetime.now().date(),
                                                              totalPrice=item['totalPrice'],
                                                              unitPrice=item['unitPrice'],
                                                              updateTime=datetime.now())
        sqlHouseDetailInfoF = sqlHouseDetailInfo.format(houseId=item['houseCode'], date=datetime.now().date(),
                                                        houseNumType=item['houseNumType'],
                                                        houseHeight=item['houseHeight'],
                                                        houseBigSquare=item['houseBigSquare'],
                                                        houseInnerSquare=item['houseInnerSquare'],
                                                        houseStuctType=item['houseStuctType'],
                                                        houseDirctionType=item['houseDirctionType'],
                                                        houseStuctMaterialType=item['houseStuctMaterialType'],
                                                        houseDecrateType=item['houseDecrateType'],
                                                        houseIsWithLift=item['houseIsWithLift'],
                                                        houseRightYear=item['houseRightYear'],
                                                        tradeOnlineTime=item['tradeOnlineTime'],
                                                        tradeRightType=item['tradeRightType'],
                                                        tradeLastTime=item['tradeLastTime'],
                                                        tradeUseType=item['tradeUseType'],
                                                        tradeLostTime=item['tradeLostTime'],
                                                        tradeHouseRightOwnType=item['tradeHouseRightOwnType'],
                                                        tradeGurantyMsg=item['tradeGurantyMsg'],
                                                        tradeHouseBookMsg=item['tradeHouseBookMsg'])
        print(sqlHouseEveryDayPriceF)
        print(sqlHouseBaseInfoF)
        print(sqlHouseDetailInfoF)

        conn.execute(sqlHouseEveryDayPriceF)
        conn.execute(sqlHouseBaseInfoF)
        conn.execute(sqlHouseDetailInfoF)
        conn.commit();


        self.logger.info("**********************inset into sql ok********************")
        return item
