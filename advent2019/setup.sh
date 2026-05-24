#!/bin/bash

number=$1
cp ../template.py ${number}.py
touch ${number}_dat.txt
sed -i "" "s/1_dat.txt/${number}_dat.txt/g" ${number}.py
# open -a /Applications/Sublime\ Text.app ../helper.py ${number}.py ${number}_dat.txt
python3 ${number}.py
echo "python3 ${number}.py"
