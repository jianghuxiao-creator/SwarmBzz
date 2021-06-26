#!/usr/bin/python3

import pymysql
# This is a sample Python script.
import os
import re
import subprocess
from re import Match
from pymysql.converters import escape_string

# 打开数据库连接
db = pymysql.connect(host='8.211.197.109', port=3306, user='bzz', passwd='bzz', db='bzz', charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
addressRes = ""
lastchequesRes = ""
statusRes = ""
versionRes = ""
IPRResIP = ""
PeersRes = ""
existAddress = ""
f = open("./log.txt", mode='r')
IP = "echo -n IP: >> result.log>&1 && curl ifconfig.me  >> result.log>&1 && echo -n Peers: >> result.log>&1"
for line in f:
    newline = re.findall("127.0.0.1:(\d+)-", line)
    if newline:
        Port = newline.pop(0)
        clearCommand = "> result.log"
        connectCountR = "`curl -s http://localhost:" + Port + "/peers | jq '.peers | length'  >> result.log>&1`"
        addressR = "`curl localhost:" + Port + "/addresses | jq | grep ethereum >> result.log>&1`"
        chequeR = "`curl localhost:" + Port + "/chequebook/cheque | jq >> result.log>&1`"
        statusCommand = "`curl http://localhost:1635/health >> result.log>&1`"
        print(connectCountR)
        subprocess.getstatusoutput(clearCommand)
        subprocess.getstatusoutput(IP)
        subprocess.getstatusoutput(connectCountR)
        subprocess.getstatusoutput(addressR)
        subprocess.getstatusoutput(chequeR)
        subprocess.getstatusoutput(statusCommand)
        flog = open("./result.log", mode='r')
        for linelog in flog:
            IPTemp = re.findall(".*IP:(.*)", linelog)
            if IPTemp:
               IPRRes = IPTemp.pop(0)
            PeersTemp = re.findall(".*(.*)Peers:.*", linelog)
            if PeersTemp:
               PeersRes = PeersTemp.pop(0)
            addressTemp = re.findall(".*ethereum(.*)", linelog)
            if addressTemp:
                addressRes = addressTemp.pop(0)
            lastchequesTemp = re.findall(".*lastcheques(.*)", linelog)
            if lastchequesTemp:
                lastchequesRes = lastchequesTemp.pop(0)
            statusTemp = re.findall(".*status(.*)", linelog)
            if statusTemp:
                statusRes = statusTemp.pop(0)
            versionTemp = re.findall(".*version(.*)", linelog)
            if statusTemp:
                versionRes = versionTemp.pop(0)
        addressRes = addressRes[4:46]
        print("IP:"+IPRRes)
        IPRResIP = IPRRes[:IPRRes.index("P")]
        PeersRes = IPRRes[IPRRes.index("s:")+2:]
        #print("connectCountRes:"+Peers)
        print("IP:"+IPRResIP)
        print("Peers:" + PeersRes)
        print("address:"+addressRes)
        print("lastchequesRes:"+lastchequesRes)
        print("statusRes:" + statusRes)
        print("versionRes:" + versionRes)
        sqlquery = """select address from node where (address = '%s')"""% (addressRes)
        cursor.execute(sqlquery)
        db.commit()
        results = cursor.fetchall()
        for row in results:
            existAddress = row[0]
        print("existAddress:"+existAddress)
        if existAddress == addressRes:
            sql = """update node set ip = '%s', count = '%s', cheques = '%s', status = '%s', version = '%s' where address = '%s'"""% (IPRResIP, PeersRes, lastchequesRes,statusRes,versionRes,existAddress)
        else:
            sql = """INSERT INTO node (ip, count, address, cheques, status, version) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % ( IPRResIP, PeersRes, addressRes, lastchequesRes, statusRes, versionRes)
        cursor.execute(sql)
        db.commit()
        # 使用 execute()  方法执行 SQL 查询

        # 使用 fetchone() 方法获取单条数据.

        # cursor.execute("select * from node")

        # data = cursor.fetchone

        #
# print(data)
cursor.close()
# 关闭数据库连接
db.close()
