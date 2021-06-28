#!/bin/bash

crontab -l > aa
FIND_FILE="/home/mainnet/aa"
FIND_STR="dblink.py"
# 判断匹配函数，匹配函数不为0，则包含给定字符
if [ `grep -c "$FIND_STR" $FIND_FILE` -ne '0' ];then
    echo "定时任务已设置 python3 /home/mainnet/dblink.py!"
else
	echo "定时任务未设置"
	echo "*/1 * * * * python3 /home/mainnet/dblink.py" >> aa
	crontab aa
	service cron restart
fi
