#!/bin/bash

APP_USER_NAME=maciek

[[ $(id -u) -ne $(id -u $APP_USER_NAME) ]] && exec su - $APP_USER_NAME -c "$0 $@"

python /home/maciek/sh/shread.py &
echo $! > /home/maciek/sh/shread.pid

