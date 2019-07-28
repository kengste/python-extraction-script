#!/usr/bin/sh
virtualenv venv --python=python3
source venv/bin/activate
pip3 install nltk
export NLTK_DATA='./nltk_data'
pip3 freeze > requirements.txt
python3 index.py

# cat << EOF
# Please proceed to restore databases using azure data studio GUI!
# EOF