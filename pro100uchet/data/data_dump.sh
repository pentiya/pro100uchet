#!/bin/sh

options="--indent 2"
tables="auth.user rzd.doroga rzd.region rzd.station"
for table in $tables
do
  echo domp table $table
  ./manage.py dumpdata $options $table > data/$table.json
done

#./manage.py dumpdata $options > data/full_dump.json
