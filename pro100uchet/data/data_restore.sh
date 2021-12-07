#!/bin/sh

#options="--indent 2"
tables="auth.user rzd.doroga rzd.region rzd.station"
for table in $tables
do
  echo restore table $table
  ./manage.py loaddata data/$table.json
done