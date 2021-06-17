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
        IP = "`curl ifconfig.me`"
        Port = newline.pop(0)
        connectCount = "·curl -s http://localhost:" + Port + "/peers | jq '.peers | length'"
        # address ="`curl localhost:" + Port + "/addresses | jq | grep ethereum`"
        # publicKey ="`curl localhost:" + Port + "/addresses | jq | grep publicKey`"
        # pssPublicKey ="`curl localhost:" + Port + "/addresses | jq | grep pssPublicKey`"
        # balance ="`curl localhost:" + Port + "/chequebook/balance | jq`"
        # cheque ="`curl localhost:" + Port + "/chequebook/cheque | jq`"
        print(connectCount)
        IP = subprocess.getstatusoutput(IP)
        # connectCountRes = subprocess.getstatusoutput(connectCount)
        # address = subprocess.getstatusoutput(address)
        # publicKey = subprocess.getstatusoutput(publicKey)
        # pssPublicKey = subprocess.getstatusoutput(pssPublicKey)
        # balance = subprocess.getstatusoutput(balance)
        # cheque = subprocess.getstatusoutput(cheque)
        IP = IP[1]
        # connectCountRes = connectCountRes[1]
        # address = address[1]
        # publicKey = publicKey[1]
        # pssPublicKey = pssPublicKey[1]
        # balance = balance[1]
        # cheque = cheque[1]
        # print(IP)
        print(connectCountRes)
        # print(address)
        # print(publicKey)
        # print(pssPublicKey)
        # print(balance)
        # print(cheque)
        sql = "INSERT INTO node (id, ip, count, ethereum, publicKey, pssKey, totalBalance, availableBalance, totalCheque, chequeId) VALUES (38, %s, %s, %s, %s, %s, %s, %s, '0', NULL)"%(IP,connectCountRes,address,publicKey,pssPublicKey,balance,cheque)
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
