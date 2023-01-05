#!/bin/bash

: <<'END'
I only test for python 3 avilability because I only tested my code running with that version,
and if someone uses python alias python3, pip3 commands still work.
END

# this fuction will install brew if missing
function install_brew_if_needed {
  if ! [[ -x "$(command -v brew)" ]]
  then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  fi

  return $?
}


# this function will install python3 under brew
function install_python {
  # update brew
  brew update

  # install Python 3
  brew install python

  return $?
}


if ! [[ -x "$(command -v python3)" ]]
then
  echo 'It looks like Python3 is not installed on your computer, let me try to fix that for you.'
  install_brew_if_needed
  test $? -ne 0 && echo "ERROR: installing brew had problems, will not continue" && exit 100

  install_python
  test $? -ne 0 && echo "ERROR: installing python3 had problems, will not continue" && exit 100
fi

if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'There is no pip3 installed on your computer, please check your python3 install.'
  exit 100
fi

if ! [[ -x "$(command -v python3 -m venv)" ]]
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
