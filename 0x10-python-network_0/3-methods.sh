#!/bin/bash
# do something
curl -s -X OPTIONS -I "$1" | grep -i "Allow:" |  awk -F ": " '{print $2}'
