DROP TABLE IF EXISTS houseData;
CREATE TABLE houseData(
id INTEGER PRIMARY KEY AUTOINCREMENT,
houseCode INT ,
houseInfo TEXT,-- 房屋的基本信息
totalPrice FLOAT ,--   整套房子的总价个
publishday INT DEFAULT 0,----一共发布了多少天
url TEXT,----详情连接地址
visited int,--当前共计多少访问量
region TEXT,-- 地区分布
attention INT ,--   关注度
unitPrice FLOAT, ---每平方米单价
recordTime DATETIME---
);