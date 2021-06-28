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

python3 dblink.py

FIND_FILE="/home/mainnet/aa"
FIND_STR="dblink.py"
crontab -l > aa
# 判断匹配函数，匹配函数不为0，则包含给定字符
if [ `grep -c "$FIND_STR" $FIND_FILE` -ne '0' ];then
    echo "定时任务已设置 python3 /home/mainnet/dblink.py!"
else
	echo "定时任务未设置"
	echo "*/1 * * * * python3 /home/mainnet/dblink.py" >> aa
	crontab aa
	service cron restart
fi
