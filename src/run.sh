#!/bin/bash

if ! [[ -x "$(command -v venv/bin/pip3)" ]]
then
  ~/.local/bin/virtualenv venv
  venv/bin/pip3 install -r requirements.txt
fi

venv/bin/python3 battleship.py