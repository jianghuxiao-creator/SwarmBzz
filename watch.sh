#!/bin/bash

pip install pymysql

rm dblink.py

wget https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/dblink.py

> log.txt

docker-compose ps >log.txt 2>&1

apt install -y jq

python3 dblink.py && rm aa


crontab -l > aa
echo "*/1 * * * * python3 /home/mainnet/dblink.py" >> aa
crontab aa
service cron restart
