#!/usr/bin/python3

import pymysql
# This is a sample Python script.
import os
import re
import subprocess
from re import Match
# 打开数据库连接
db = pymysql.connect(host='8.211.197.109', port=3306, user='bzz', passwd='bzz', db='bzz', charset='utf8')


# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

f = open("./log.txt", mode='r')
id = 7
for line in f:
    newline = re.findall("127.0.0.1:(\d+)-", line)
    if newline:
        connectCount = "curl -s http://localhost:" + newline.pop(0) + "/peers | jq '.peers | length'"
        print(connectCount)
        connectCountRes = subprocess.getstatusoutput(connectCount)
        print(connectCountRes)
        connectCountRes = re.findall("'(\d+)'", connectCountRes)
        connectCountRes2 = connectCountRes.pop(0)
        print(connectCountRes2)
        sql = "INSERT INTO node (id, ip, count, ethereum, publicKey, pssKey, totalBalance, availableBalance, totalCheque, chequeId) VALUES (28, '47.254.29.63', %s, '0x2c5557276d348e39724041f3beaa21fc70831b2a', '02e6e15ec6e2c476f0eac2d8ab90c630c78804523f21f7bdfcef08dafa564539dd', '0389a677ee0fbf5b8bf9e25b61b8b024ff259b68225f2d8f5e34049981d76c21dc', '1e+16', '1e+16', '0', NULL)"%(connectCountRes)
        cursor.execute(sql)
        db.commit()
        id=id+1
# 使用 execute()  方法执行 SQL 查询


# 使用 fetchone() 方法获取单条数据.


#cursor.execute("select * from node")

#data = cursor.fetchone

#
#print(data)
cursor.close()
# 关闭数据库连接
db.close()


# ip=`curl ifconfig.me`
# connectCount=`curl -s http://localhost:1635/peers | jq '.peers | length' `
# address=`curl localhost:1635/addresses | jq | grep ethereum`
# publicKey=`curl localhost:1635/addresses | jq | grep publicKey`
# pssPublicKey=`curl localhost:1635/addresses | jq | grep pssPublicKey`
# balance=`curl localhost:1635/chequebook/balance | jq`
# cheque=`curl localhost:1635/chequebook/cheque | jq`
