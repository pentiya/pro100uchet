#!/bin/sh

#options="--indent 2"
tables="rzd.doroga rzd.otdelenie rzd.station"
for table in $tables
do
  echo restore table $table
  ./manage.py loaddata data/$table.json
done