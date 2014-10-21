echo Cleaning up --------------

rm -r *.txt
rm -r *.tmp
rm -r *.csv

echo Download data ------------

curl https://github.com/zonca/swcarpentry-workshop-pandas/blob/master/rawdata/rawdata.zip?raw=true -o rawdata.zip -L

echo unpack -------------------

unzip rawdata.zip

rm -r rawdata.zip
rm -r *.tmp

echo rename --------------------

for f in *.txt
do
	mv  $f ${f/txt/csv}
done


echo Available csv files -------

ls *csv 