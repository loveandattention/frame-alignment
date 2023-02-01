#!/bin/bash

flaskpid=`ps -aux | grep app.py | grep -v grep | wc -l | sed -e 's/^[ \t]*//'`
if [[ "$flaskpid" != "0" ]]
then
	echo "------- RestartServer Is Running ---------"
	ps -aux | grep app.py | $grepapps | grep -v grep
	echo "-----------------------------------"
	echo "Force Rebooting..."
	ps -aux | grep app.py | grep -v grep | awk '{ printf $2 }' | xargs kill -9
fi
nohup python3 app.py >../../shell/linux/log/frame_flask.log 2>&1 &
