#!/usr/bin/env bash
wget -nc http://nlp.stanford.edu/software/stanford-ner-2015-12-09.zip
unzip stanford-ner-2015-12-09.zip
mv stanford-ner-2015-12-09 stanford-ner
echo "Google bought IBM for $10." > samples.txt
python main.py -f samples.txt -v
rm stanford-ner-2015-12-09.zip
