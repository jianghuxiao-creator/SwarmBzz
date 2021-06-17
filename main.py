# This is a sample Python script.
import os
import re
from re import Match

f = open("./log.txt", mode='r')

#
# ip=`curl ifconfig.me`
# connectCount=`curl -s http://localhost:1635/peers | jq '.peers | length' `
# address=`curl localhost:1635/addresses | jq | grep ethereum`
# publicKey=`curl localhost:1635/addresses | jq | grep publicKey`
# pssPublicKey=`curl localhost:1635/addresses | jq | grep pssPublicKey`
# balance=`curl localhost:1635/chequebook/balance | jq`
# cheque=`curl localhost:1635/chequebook/cheque | jq`
#

for line in f:
    newline = re.findall("127.0.0.1:(\d+)-", line)
    if newline:
        IP = "`curl ifconfig.me`"
        connectCount = "curl -s http://localhost:"+newline.pop(0)+"/peers | jq '.peers | length'"
        address = "`curl localhost:"+newline.pop(0)+"/addresses | jq | grep ethereum`"
        publicKey = "`curl localhost:"+newline.pop(0)+"/addresses | jq | grep publicKey`"
        pssPublicKey = "`curl localhost:"+newline.pop(0)+"/addresses | jq | grep pssPublicKey`"
        balance = "`curl localhost:"+newline.pop(0)+"/chequebook/balance | jq`"
        cheque = "`curl localhost:"+newline.pop(0)+"/chequebook/cheque | jq`"
        os.system(IP)
        os.system(connectCount)
        os.system(address)
        os.system(publicKey)
        os.system(pssPublicKey)
        os.system(balance)
        os.system(cheque)



