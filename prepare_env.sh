#!/usr/bin/env bash

PY_VER=$(python --version | grep -o -e "3\..")

if [ ! "$PY_VER" == "3.5" ]; then
  echo "Python 3.5 is mandatory."
  exit 1
fi

virtualenv venv.
source venv/bin/activate
pip install -r requirements.txt
