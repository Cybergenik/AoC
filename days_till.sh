#!/bin/bash
#
# Lil program to tell me how close we are to the annual AoC 
#
# By: Luciano Remes
##
AOC=`date +%Y`1201
s_AOC=`date +%s -d $AOC`
today=`date +%s`
DATE=$((($s_AOC-$today) / 86400))
if [ $DATE -eq 1 ]; then
    echo "$DATE day till AoC! tonight at 10pm MT/12pm EST!"
elif [ $DATE -le 0 ]; then
    echo "It's AoC!"
    sleep .5
    for i in {1..40}
    do
        printf "A"
        sleep .08
    done
    printf "hhh\n" 
    sleep .5
    echo "nandaaayou :>"
else
    echo "$DATE days till AoC"
fi
