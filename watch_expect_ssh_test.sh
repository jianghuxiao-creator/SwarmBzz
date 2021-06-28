#!/usr/bin/env expect

set HOST [lindex $argv 0]
set PASSWD [lindex $argv 1]
spawn ssh -o StrictHostKeyChecking=no root@$HOST
expect  "(yes/no)?" { send "yes\n" }
expect "*password:" { send "$PASSWD\n" }
expect "*password:" { send "$PASSWD\n" }
expect "*#" { send "cd /home/mainnet;rm watch.sh;wget https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/watch.sh && chmod a+x watch.sh && ./watch.sh\n" }
expect "*#" { send "cd /home/mainnet;rm crontabexcute.sh;wget https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/crontabexcute.sh && chmod a+x crontabexcute.sh && ./crontabexcute.sh\n" }
expect eof
