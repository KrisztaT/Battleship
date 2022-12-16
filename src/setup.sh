#!/bin/bash

: <<'END'
I only test for python 3 avilability because I only tested my code running with that version,
and if someone uses python alias python3, pip3 commands still work.
END

if  ! [[ -x "$(command -v python3)" ]]
then
  echo 'It looks like Python3 is not installed on your computer, let me fix that for you.'
  sudo apt-get install python3
fi

if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'There is no pip3 installed on your computer, let me install it for you.' 
  sudo apt install python3-pip
fi

if ! [[ -x "$(command -v ~/.local/bin/virtualenv)" ]]
then
  echo 'It looks like virtual environment is not installed on your computer, let me do it for you.'
  pip3 install virtualenv
fi

~/.local/bin/virtualenv venv
venv/bin/pip3 install -r requirements.txt

venv/bin/python3 battleship.py