# coding=utf-8
import sqlite3

import os

# print os.path.join(os.pardir(__file__), 'house.db')
import MySQLdb

pardir = os.path.dirname(os.path.realpath(__file__))
print(os.path.dirname(__file__))
DATABASE = os.path.join( pardir , 'house.db')
DATABASE = r"D:\projects\github\rentPhoneServerManager\db\house.db";

conn = MySQLdb.connect("192.168.1.112", "admin", "Huawei123", "adminserver", charset='utf8' )


# conn = sqlite3.connect(DATABASE)
def getDb():
  return conn
def create_db():
  # 连接
  conn = sqlite3.connect(DATABASE)
  c = conn.cursor()
  with open('db.sql','r') as f:
    c.executescript(f.read());

  # 提交！！！
  conn.commit()
  # 关闭
  conn.close()

if __name__ == '__main__':
    create_db()