#!/usr/bin/env bash
# MD5 (stanford-ner-2015-12-09.zip) = 18fb7a76a930e270eb261cbcfb993067
# wget -nc http://nlp.stanford.edu/software/stanford-ner-2015-12-09.zip
rm -rf stanford-ner-2015-12-09.zip # if any.
cat stanford-ner-2015-12-09.zip* > stanford-ner-2015-12-09.zip
unzip stanford-ner-2015-12-09.zip
mv stanford-ner-2015-12-09 stanford-ner
echo "Google bought IBM for 10 dollars. Mike was happy about this deal." > samples.txt
python main.py -f samples.txt -v
rm stanford-ner-2015-12-09.zip
