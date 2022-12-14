#!/bin/bash

if  ! [[ -x "$(command -v python3)" ]]
then
  echo 'It looks like Python is not installed.
    To install Python, check out https://www.python.org/downloads/'
  exit 1
fi

if ! [[ -x "$(command -v pip)" ]]
then
  echo 'There is no pip installed, let me do it for you.' 
  sudo apt install python3-pip
fi

if ! [[ -x "$(command -v ~/.local/bin/virtualenv)" ]]
then
  echo 'It looks like virtual environment is not installed, let me do it for you.'
  pip install virtualenv
fi

~/.local/bin/virtualenv venv
venv/bin/pip install tabulate
venv/bin/pip install termcolor
venv/bin/pip install pyfiglet
venv/bin/pip install regex
venv/bin/pip install pytest
venv/bin/python3 battleship.py