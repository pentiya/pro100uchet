#!/bin/sh

options="--indent 2"
tables="rzd.doroga rzd.otdelenie rzd.station"
for table in $tables
do
  echo domp table $table
  ./manage.py dumpdata $options $table > data/$table.json
done