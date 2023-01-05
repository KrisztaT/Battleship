#!/bin/bash

: <<'END'
I only check for python3 avilability because I  tested my code running with that version,
and if someone uses python alias python3, pip3 commands still work.
END

if  ! [[ -x "$(command -v python3)" ]]
then
  echo 'It looks like Python3 is not installed on your computer, let me fix that for you.'
  sudo apt install python3
  test $? -ne 0 && echo "ERROR: installing python3 had problems, will not continue" && exit 100
fi

if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'There is no pip3 installed on your computer, let me install it for you.' 
  sudo apt install python3-pip
  test $? -ne 0 && echo "ERROR: installing pip3 had problems, will not continue" && exit 100
fi

if ! (pip3 show virtualenv &>/dev/null)
then
  echo 'It looks like virtual environment is not installed on your computer, let me do it for you.'
  pip3 install virtualenv
  test $? -ne 0 && echo "ERROR: installing virtualenv had problems, will not continue" && exit 100
fi

python3 -m venv ./venv
test $? -ne 0 && echo "ERROR: configuring virtualenv had problems, will not continue" && exit 100
venv/bin/pip3 install -r requirements.txt
test $? -ne 0 && echo "ERROR: installing pip packages had problems, will not continue" && exit 100

venv/bin/python3 battleship.py