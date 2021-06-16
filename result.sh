#!/bin/bash
apt install -y jq
ip=`curl ifconfig.me`
connectCount=`curl -s http://localhost:1635/peers | jq '.peers | length' `
address=`curl localhost:1635/addresses | jq | grep ethereum`
publicKey=`curl localhost:1635/addresses | jq | grep publicKey`
pssPublicKey=`curl localhost:1635/addresses | jq | grep pssPublicKey`
balance=`curl localhost:1635/chequebook/balance | jq`
cheque=`curl localhost:1635/chequebook/cheque | jq`

rm -r logs
mkdir logs
a=`curl ifconfig.me`
echo $ip >>/home/bee/logs/${a}-bee_console.log>&1
echo $connectCount >>/home/bee/logs/${a}-bee_console.log>&1
echo $address >>/home/bee/logs/${a}-bee_console.log>&1
echo $publicKey >>/home/bee/logs/${a}-bee_console.log>&1
echo $pssPublicKey >>/home/bee/logs/${a}-bee_console.log>&1
echo $balance >>/home/bee/logs/${a}-bee_console.log>&1
echo $cheque >>/home/bee/logs/${a}-bee_console.log>&1
docker-compose logs --tail="10" >>/home/bee/logs/bee_console.log>&1

apt -y install expect
expect -c "
spawn scp -o StrictHostKeyChecking=no -r /home/bee/logs  root@8.208.115.2:/home
expect {   
    \"*assword\"
                {
                    set timeout 300;
                    send \"YcYsf88*\r\";
                }
    \"yes/no\"
                {
                    send \"yes\r\"; exp_continue;}
                }
expect eof"
