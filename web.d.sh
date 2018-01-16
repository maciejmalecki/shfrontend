#!/bin/sh

APP_USER_NAME=maciek

[[ $(id -u) -ne $(id -u $APP_USER_NAME) ]] && exec su - $APP_USER_NAME -c "$0 $@"

python /home/maciek/sh/web.py 8080 >/home/maciek/sh/web.log 2>/home/maciek/sh/web.err.log &
echo $! > /home/maciek/sh/shweb.pid

