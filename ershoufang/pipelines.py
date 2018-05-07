# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3

from datetime import datetime
from conf.logControl import logControl
from db.dbInit import DBUTIl


class ErshoufangPipeline(object):
    conn = DBUTIl.getDBConn()
    logger = logControl.getLogger()
    c = conn.cursor();

    sqlHouseBaseInfo = u"replace into houseBaseInfo (houseCode,url,visited,region,area,attention,sourceId) values ('{houseCode}','{url}','{visited}','{region}','{area}','{attention}','{sourceId}')";
    sqlHouseEveryDayPrice = u"replace into houseEveryDayPrice (houseCode,updateDay,totalPrice,unitPrice,updateTime) values ('{houseCode}','{date}','{totalPrice}','{unitPrice}','{updateTime}')";
    sqlHouseDetailInfo = u"replace into houseDetailInfo (houseCode,updateDay,houseNumType,houseHeight,houseBigSquare,houseInnerSquare,houseStuctType,houseDirctionType,houseStuctMaterialType,houseDecrateType,houseIsWithLift,houseRightYear,tradeOnlineTime,tradeRightType,tradeLastTime,tradeUseType,tradeLostTime,tradeHouseRightOwnType,tradeGurantyMsg,tradeHouseBookMsg) values ('{houseId}','{date}','{houseNumType}','{houseHeight}','{houseBigSquare}','{houseInnerSquare}','{houseStuctType}','{houseDirctionType}','{houseStuctMaterialType}','{houseDecrateType}','{houseIsWithLift}','{houseRightYear}','{tradeOnlineTime}','{tradeRightType}','{tradeLastTime}','{tradeUseType}','{tradeLostTime}','{tradeHouseRightOwnType}','{tradeGurantyMsg}','{tradeHouseBookMsg}')"


    def process_item(self, item, spider):


        self.logger.info("#############process_item start###############")


        self.logger.info("#############preparing sql statements###############")
        sqlHouseBaseInfoF = self.sqlHouseBaseInfo.format(houseCode=item['houseCode'],

                                                    url=item['url'],
                                                    visited=item['visited'],
                                                    region=item['region'],
                                                    area=item['area'],
                                                    attention=item['attention'],
                                                    sourceId=item['sourceId']
                                                    )
        sqlHouseEveryDayPriceF = self.sqlHouseEveryDayPrice.format(houseCode=item['houseCode'],
                                                              date=datetime.now().date(),
                                                              totalPrice=item['totalPrice'],
                                                              unitPrice=item['unitPrice'],
                                                              updateTime=datetime.now())
        sqlHouseDetailInfoF = self.sqlHouseDetailInfo.format(houseId=item['houseCode'], date=datetime.now().date(),
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
        self.logger.info(sqlHouseEveryDayPriceF)
        # print(sqlHouseBaseInfoF)
        self.logger.info(sqlHouseDetailInfoF)
        try:
            self.c.execute(sqlHouseEveryDayPriceF)
            self.c.execute(sqlHouseBaseInfoF)
            self.c.execute(sqlHouseDetailInfoF)

            self.conn.commit();
        except Exception as e:
            self.logger.exception(e)


        self.logger.info("**********************inset into sql ok********************")
        return item
