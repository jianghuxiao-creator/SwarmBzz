pip install pymysql

wget https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/dblink.py

docker-compose ps >log.txt 2>&1

python3 dblink.py

crontab -l > aa
echo "*/1 * * * * python3 /home/mainnet/dblink.py" >> aa
crontab aa
