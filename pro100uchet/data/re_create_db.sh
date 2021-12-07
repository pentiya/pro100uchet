#/bin/sh

echo del db and migrations


cd ..
ls -1




project=pro100uchet
apps='device gvc rzd'

rm $project/__pycache__/*
rmdir $project/__pycache__

for i in $apps
do
echo $i
rm $i/__pycache__/*
rmdir $i/__pycache__

rm $i/migrations/__pycache__/*
rmdir $i/migrations/__pycache__

rm $i/migrations/*
#rm $i/migrations/0*.py
rmdir $i/migrations

done

rm db.sqlite3

./manage.py makemigrations
./manage.py makemigrations device
./manage.py makemigrations gvc
./manage.py makemigrations rzd

./manage.py migrate

#./make_migration.sh
#./manage.py makemigrations
#./manage.py migrate


data/data_restore.sh

cd ..

exit

