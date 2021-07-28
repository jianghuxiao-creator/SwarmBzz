#!/usr/bin/python3

import pymysql
# This is a sample Python script.
import os
import re
import subprocess
from re import Match
import time  # 引入time模块
import sched
from pymysql.converters import escape_string
from datetime import datetime
schedule = sched.scheduler(time.time, time.sleep)
def insert(inc):
# 打开数据库连接
    db = pymysql.connect(host='47.117.1.214', port=3306, user='ycdev-test', passwd='ycdev-test', db='testdata', charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    addressRes = ""
    lastchequesRes = ""
    statusRes = ""
    versionRes = ""
    IPRResIP = ""
    PeersRes = ""
    existAddress = ""

    now = int(round(time.time()*1000))
    ticks = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now/1000))
    print( "当前时间戳为:", ticks)
    subprocess.getstatusoutput("docker-compose ps > log.txt")
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
            statusCommand = "`curl http://localhost:" + Port + "/health >> result.log>&1`"
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
            print("port:"+Port)
            sqlquery = """select address from bzz_node where (address = '%s')"""% (addressRes)
            cursor.execute(sqlquery)
            db.commit()
            results = cursor.fetchall()
            for row in results:
                existAddress = row[0]
            print("existAddress:"+existAddress)
            if existAddress == addressRes:
                sql = """update bzz_node set ip = '%s', count = '%s', cheques = '%s', status = '%s', version = '%s',update_time = '%s',port='%s' where address = '%s'"""% (IPRResIP, PeersRes, lastchequesRes,statusRes,versionRes,ticks,Port,existAddress)
            else:
                sql = """INSERT INTO bzz_node (ip, count, address, cheques, status,create_time, version,port) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % ( IPRResIP, PeersRes, addressRes, lastchequesRes, statusRes, ticks,versionRes,Port)
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
    schedule.enter(inc, 0, insert, (inc,))
def main(inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    schedule.enter(0, 0, insert, (inc,))
    schedule.run()
# 10s 输出一次
main(60)
