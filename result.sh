#!/bin/bash
ip=`curl ifconfig.me`
connectCount=`curl -s http://localhost:1635/peers | jq '.peers | length' `
address=`curl localhost:1635/addresses | jq | grep ethereum`
address=`curl localhost:1635/addresses | jq | grep ethereum`
balance=`curl localhost:1635/chequebook/balance | jq`
cheque=`curl localhost:1635/chequebook/cheque | jq`

echo $ip
echo $connectCount
echo $address
echo $balance
echo $cheque
