pip install pymysql

wget https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/dblink.py

docker-compose ps >log.txt 2>&1

python3 dblink.py

echo "*/1 * * * * python3 /home/mainnet/dblink.py" >> /var/spool/cron/root
