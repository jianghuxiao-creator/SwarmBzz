#!/usr/bin/env expect

set HOST [lindex $argv 0]
set PASSWD [lindex $argv 1]
spawn scp -r root@$HOST:/home/bee/logs /home/
expect "*password:" { send "$PASSWD\n" }
expect eof
