#!/bin/sh
echo "azurite is starting..."
azurite --silent &

#we should make container wait for our service or it will be killed immediately 
sleep 2