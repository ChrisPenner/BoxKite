#!/bin/sh
echo 'Starting App Server at localhost:8080'
dev_appserver.py app.yaml &
echo 'Waiting for app server to start...'
# If getting "Connection refused error" increase sleep time.
sleep 5
echo "Crawling site..."
wget -P ./static-site/ -mpck --user-agent="" -e robots=off --wait 1 -E localhost:8080/
trap 'kill $(jobs -p)' EXIT
