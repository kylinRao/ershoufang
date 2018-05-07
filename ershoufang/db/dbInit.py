# coding=utf-8
import sqlite3

import os

# print os.path.join(os.pardir(__file__), 'house.db')
import MySQLdb

class DBUTIl:
    DATABASE = r"D:\projects\github\rentPhoneServerManager\db\house.db";
    conn = MySQLdb.connect("192.168.1.112", "admin", "Huawei123", "adminserver", charset='utf8' )
    @staticmethod
    def getDBConn():
        try:
            DBUTIl.conn.ping()
        except:
            print 'mysql connect have been close'
            DBUTIl.conn = MySQLdb.connect("192.168.1.112", "admin", "Huawei123", "adminserver", charset='utf8' )
        return DBUTIl.conn