#!/bin/sh

for year in 2014 2015 2016 2017 2018 2019
do
    for file in /home/ramgyl/Documents/CS685A/Project/ncrb_test/"$year"/*
    do
        name=$(echo "$file" | rev | cut -f 1 -d '/' | rev)
        cat "$file" > temp1.csv
        extension=$(echo "$name" | cut -f 2 -d '.')
        if [[ "$extension" = "xls" ]]
        then
            xls2csv "$file" > temp1.csv
        else
            xlsx2csv "$file" > temp1.csv
        fi
        sed -i 's/\"//g' temp1.csv
        sed -i '/^$/d' temp1.csv
        sed -i '/State:\|Total District(s),\|Source:\|Total,,\|Total,[[:digit:]]\|State :\|UT :/d' temp1.csv
        sed -i '1d' temp1.csv
        if [[ $year -gt 2016 ]]
        then    
            sed -i '$d' temp1.csv
        fi
        newname=$(echo "$name" | cut -f 1 -d '.')"_$year"
        if [[ $year -gt 2016 ]]
        then
            cut -f 2- -d ',' temp1.csv | tr -s " " | sed 's/,*$//g' | sed '/^$/d' > ./"$year"/"$newname".csv
        else
            cut -f 2,4- -d ',' temp1.csv | tr -s " " | sed 's/,*$//g' | sed '/^$/d' > ./"$year"/"$newname".csv
        fi
    done
done

rm -rf temp1.csv