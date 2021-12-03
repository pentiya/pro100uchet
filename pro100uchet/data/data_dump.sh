#!/bin/sh

options="--indent 2"
tables="rzd.doroga rzd.otdelenie rzd.stanciya"
for table in $tables
do
  echo domp table $table
  ./manage.py dumpdata $options $table > data/$table.json
done