#!/usr/bin/env bash
#
# This script can be used to sync the wiki submodule
# in case you're using github internal wiki option
#

git pull origin master
cd wiki || return
git pull origin master
cd .. || return
git commit -a -m "updated wiki"
git push origin master
