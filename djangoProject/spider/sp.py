import pymysql
from pyhive import hive
from pyhive import hive
import pandas as pd
conn = hive.connect(host="192.168.170.133",port=10000, auth="LDAP", database="default",username="root",password="123456")
query_sql = "select * from goods"
curosr = conn.cursor()
curosr.execute(query_sql)

clumns = curosr.description
# ('华为智慧屏 SE 55英寸 超薄电视 广色域鸿鹄画质 4K超高清智能液晶电视机 HD55DESA 2+16GB搭载 HarmonyOS 2', 1499.0, '华为京东自营官方旗舰店', 200000)
data = pd.DataFrame()
# 获取全部数据，result是tuple
for result in curosr.fetchall():
    data.append(pd.DataFrame(list(result)))

curosr.close()
