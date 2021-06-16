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
