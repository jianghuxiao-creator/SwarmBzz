#!/bin/bash

pip install pymysql

rm dblink.py

wget https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/dblink.py

> log.txt

docker-compose ps >log.txt 2>&1

if ! type jq >/dev/null 2>&1; then
    echo 'jq 未安装';
  	apt install -y jq
else
    echo 'jq 已安装';
fi

nohup python3 dblink.py >schedule.log &

