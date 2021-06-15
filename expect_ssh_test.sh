#!/usr/bin/env expect

set HOST [lindex $argv 0]
set PASSWD [lindex $argv 1]
spawn ssh -o StrictHostKeyChecking=no root@$HOST
expect  "(yes/no)?" { send "yes\n" }
expect "*password:" { send "$PASSWD\n" }
expect "*password:" { send "$PASSWD\n" }
expect "*#" { send "cd /home/bee;wget https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/result.sh && chmod a+x result.sh && >
expect eof

