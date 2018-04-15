
DROP TABLE IF EXISTS houseBaseInfo;
CREATE TABLE houseBaseInfo(
id INTEGER PRIMARY KEY AUTOINCREMENT,
houseCode INT UNIQUE ,
houseInfo TEXT,-- 房屋的基本信息
publishday INT DEFAULT 0,----一共发布了多少天
url TEXT,----详情连接地址
visited int,--当前共计多少访问量
region TEXT,-- 地区分布
area TEXT,---分区，如鼓楼，等
attention INT ,--   关注度
sourceId int---数据来自于哪个房产交易所
);
DROP TABLE IF EXISTS houseSource;
CREATE TABLE houseSource(
sourceId INTEGER PRIMARY KEY AUTOINCREMENT,
sourceDes TEXT-------鼓楼 建邺 秦淮 玄武 雨花台 栖霞 江宁 浦口 六合 溧水 高淳
);


DROP TABLE IF EXISTS houseEveryDayPrice;
CREATE TABLE houseEveryDayPrice(
id INTEGER PRIMARY KEY AUTOINCREMENT,
houseCode INT ,
date date,-- 房屋价格记录的当天
totalPrice FLOAT ,--   整套房子的总价个
unitPrice FLOAT,---每平方米单价/
updateTime datetime
);
create unique index houseId_date on houseEveryDayPrice(houseCode,date);
-- 统计报表
DROP TABLE IF EXISTS houseReduceDay;
CREATE TABLE houseReduceDay(
id INTEGER PRIMARY KEY AUTOINCREMENT,
houseId INT ,
date date,-- 房屋价格记录的当天
reducePercent FLOAT -- 降价百分比
);
DROP TABLE IF EXISTS houseReduceWeek;
CREATE TABLE houseReduceWeek(
id INTEGER PRIMARY KEY AUTOINCREMENT,
houseId INT ,
date date,-- 房屋价格记录的当天
reducePercent FLOAT -- 降价百分比
);
DROP TABLE IF EXISTS houseReduceMonth;
CREATE TABLE houseReduceMonth(
id INTEGER PRIMARY KEY AUTOINCREMENT,
houseId INT ,
date date,-- 房屋价格记录的当天
reducePercent FLOAT -- 降价百分比
);
DROP TABLE IF EXISTS HouseReduceUntilNow;
CREATE TABLE HouseReduceUntilNow(
id INTEGER PRIMARY KEY AUTOINCREMENT,
houseId INT ,
date date,-- 房屋价格记录的当天
reducePercent FLOAT -- 降价百分比
);
房屋详细信息表
DROP TABLE IF EXISTS houseDetailInfo;
CREATE TABLE houseDetailInfo(
id INTEGER PRIMARY KEY AUTOINCREMENT,
houseId INT UNIQUE ,
date date,-- 房屋价格记录的当天
houseNumType TEXT,---房子几室几厅
houseHeight  TEXT,-----房子楼层情况
houseBigSquare TEXT,---房子总面积
houseInnerSquare  TEXT,---房子套内面积
houseStuctType  TEXT,---房子是板楼还是调高什么的
houseDirctionType  TEXT,---房子的朝向
houseStuctMaterialType  TEXT,---房子是钢筋水泥的还是什么的
houseDecrateType  TEXT,---房子装修情况
houseIsWithLift  TEXT,---房子是否有电梯
houseRightYear  TEXT,---房子的产权一共是多少年


tradeOnlineTime  DATE ,---房子发布交易的时间
tradeRightType  TEXT,---房子的交易类型是商品房还是什么房子
tradeLastTime  DATE,---房子上次交易时间
tradeUseType  TEXT,---房子用途，一般是普通住宅
tradeLostTime  TEXT,---房子的年限是满两年还是满五年
tradeHouseRightOwnType  TEXT,---是共有产品还是什么产权房子
tradeGurantyMsg  TEXT,---房子抵押信息
tradeHouseBookMsg  TEXT---房本信息
);

































