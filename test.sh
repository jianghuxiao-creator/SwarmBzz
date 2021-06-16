#!/bin/bash

rm -r /home/logs
dir=/home/bee/result

while read line
do
host=`echo $line| awk '{print $1}'`
passwd=`echo $line | awk '{print $2}'`
$dir/expect_ssh_test.sh $host $passwd &
done < $dir/host.txt
while read line
do
host=`echo $line| awk '{print $1}'`
passwd=`echo $line | awk '{print $2}'`
$dir/passlocal.sh $host $passwd &
done < $dir/host.txt
