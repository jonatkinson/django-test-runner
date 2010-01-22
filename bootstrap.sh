#!/bin/bash
virtualenv .
source ./bin/activate
easy_install --prefix=. pip
pip install -E . -r requirements.txt
