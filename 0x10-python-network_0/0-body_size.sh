#!/bin/bash
# do something
curl -s -o /dev/null -w '%{size_download}\n' "$1"
