# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3


from datetime import datetime

from db.dbInit import conn


class ErshoufangPipeline(object):
    DATABASE = os.path.join(os.path.dirname(__file__), 'ershoufang.db')
    filePath = os.path.join(os.path.dirname(__file__), 'item.txt')

    def __init__(self):
        self.file = open(self.filePath, 'wb')

    def process_item(self, item, spider):
        print(item)
        sql = u"replace into houseData (houseCode,houseinfo,totalPrice,publishday,url,visited,region,attention,unitPrice,recordTime) values ('{houseCode}','{houseinfo}',{totalprice},'{publishday}','{url}',{visited},'{region}',{attention},{unitprice},'{recordTime}');"
        sqlF = sql.format(
            houseCode=item['houseCode'][0],
            houseinfo=item['houseInfo'][0],
            totalprice=item['totalPrice'][0],
            publishday=item['publishDay'],
            url=item['url'][0],
            visited=item['visited'],
            region=item['region'][0],
            attention=item['attention'],
            unitprice=item['unitPrice'][0],
            recordTime= datetime.now()

        );
        print(sqlF);
        conn.execute(sqlF)

        self.file.write(sql);
        conn.commit();
        return item
