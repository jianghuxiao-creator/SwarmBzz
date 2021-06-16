#!/usr/bin/env expect

expect -c "
spawn scp -r /home/bee/logs  root@8.208.115.2:/home
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
