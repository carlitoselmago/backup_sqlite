#!/bin/bash
git pull
message=${0}
git add -A
git commit -am "$message"
git push
