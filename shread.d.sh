#!/bin/bash

APP_USER_NAME=maciek

[[ $(id -u) -ne $(id -u $APP_USER_NAME) ]] && exec su - $APP_USER_NAME -c "$0 $@"

python /home/maciek/sh/shread.py >/home/maciek/sh/shread.log 2>/home/maciek/sh/shread.err.log &
echo $! > /home/maciek/sh/shread.pid

