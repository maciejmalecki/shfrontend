#!/bin/bash

APP_USER_NAME=maciek

[[ $(id -u) -ne $(id -u $APP_USER_NAME) ]] && exec su - $APP_USER_NAME -c "$0 $@"

cd /home/maciek/sh
python shread.py &
echo $! > run/shread.pid

