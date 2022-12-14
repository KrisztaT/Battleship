#!/bin/bash
chmod +x battleship.py

if  ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    It looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi

if ! [[ -x "$(command -v pip)" ]]
then
  echo 'Error: There is no pip installed, let me do it for you.' 
  sudo apt-get install python-pip
fi

if ! [[ -x "$(command -v virtualenv)" ]]
then
  echo 'Error: It looks like virtual environment is not installed, let me do it for you.'
  pip install virtualenv
fi

virtualenv venv
venv/bin/pip install tabulate
venv/bin/pip install termcolor
venv/bin/pip install pyfiglet
venv/bin/pip install regex
venv/bin/python battleship.py