#!/bin/bash

if ! [[ -x "$(command -v venv/bin/pip3)" ]]
then
  ~/.local/bin/virtualenv venv
  test $? -ne 0 && echo "ERROR: configuring virtualenv had problems, will not continue" && exit 100
  venv/bin/pip3 install -r requirements.txt
  test $? -ne 0 && echo "ERROR: configuring virtualenv had problems, will not continue" && exit 100
fi

venv/bin/python3 battleship.py