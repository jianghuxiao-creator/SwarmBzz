#!/bin/bash

pip install pymysql

rm dblink.py

wget https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/dblink.py

> log.txt

docker-compose ps >log.txt 2>&1

apt install -y jq

nohup python3 dblink.py >1.log 2>&1 && cat 1.log

