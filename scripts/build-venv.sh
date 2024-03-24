#!/bin/bash
/usr/bin/python3 -m pip install virtualenv
/usr/bin/python3 -m virtualenv venv
source venv/bin/activate
pip install -e .
pip install -r requirements.txt
