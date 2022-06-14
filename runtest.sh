#!/usr/bin/env bash

abspath="$(cd "$( dirname "$0" )" && pwd )"

# Did you install python on your machine?
if ! (type "python" >/dev/null 2>&1); then
    echo "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+"
    echo -e "ERROR:\tPython is not installed."
    echo "You need to install python to run tests."
    echo "You can easily install python using"
    echo "pyenv : https://github.com/pyenv/pyenv"
    echo " even if you are not root user."
    echo "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+"
    echo "Exit."
    exit
fi

# Did you install pytest on your machine?
if type "pytest" >/dev/null 2>&1; then
    cd "$abspath/test" || exit
    pytest # Run tests!!
else
    echo "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+"
    echo -e "Warning:\tpytest is not installed."
    echo "You must install pytest to run tests."
    echo "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+"
    read -p "Do you want to install pytest automatically? (y/N): " yn
    if [[ $yn = [yY] ]];then
        python -m pip install pytest
        echo -e "pytest installed.\nStart executing test programs!"
        cd "$abspath/test" || exit
        pytest #Run tests!
    else
        echo "Exit."
    fi
fi
