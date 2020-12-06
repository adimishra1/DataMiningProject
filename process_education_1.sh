#!/bin/sh

xls2csv 2004-05.xls > temp.csv
cat temp.csv | tr -s ' ' | sed 's/\"//g' > 2004-05.csv

# Prepare tsv by copying manually for 2010-11
cut -f 1- -d $'\t' --output-delimiter=',' 2010-11.tsv | tr -s ' ' > 2010-11.csv

xlsx2csv 2011-12.xlsx > temp.csv
cut -f 1-500 -d ',' temp.csv | tr -s ' ' > 2011-12.csv

rm -rf temp.csv