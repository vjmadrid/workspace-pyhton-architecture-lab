#!bin/bash

# ***********************
#  CONFIG GENERAL
# ***********************

PYTHON_VERSION_REQUIRED=3.9.6
PROJEC_NAME='hello-project'
VIRTUAL_ENV_NAME="venv-${PROJEC_NAME}"

echo
echo "*** CONFIG GENERAL ***"

if ! hash python; then
    echo "python is not installed"
    exit 1
fi

PYTHON_VERSION=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$PYTHON_VERSION" -lt "39" ]; then
    echo "This script requires python 3.9 or greater"
    exit 1
fi

PYTHON_VERSION=`python -c 'import platform; print(platform.python_version())'`
echo "* Python version [${PYTHON_VERSION}] is installed"

# ***********************
#  CONFIG pyenv
# ***********************

echo
echo "*** CONFIG pyenv ***"

if ! hash pyenv; then
    echo "pyenv is not installed"
    exit 1
fi

CUSTOM_PYENV_VERSION=`pyenv -v`
echo "* Pyenv version [${CUSTOM_PYENV_VERSION}] is installed"


echo "* Active pyenv local ${PYTHON_VERSION_REQUIRED}"
pyenv local $PYTHON_VERSION_REQUIRED 

echo "* Upgrading pip" 
pip install --upgrade pip

# ***********************
#  CONFIG pyenv-virtualenv
# ***********************

echo
echo "*** CONFIG pyenv virtualenvs ***"

echo "* Create virtyalenv ${VIRTUAL_ENV_NAME}"
pyenv virtualenv $PYTHON_VERSION_REQUIRED $VIRTUAL_ENV_NAME

VIRTUAL_ENV_LOCAL=`pyenv local`
echo "* Show virtyalenv ${VIRTUAL_ENV_NAME} local"

echo "* Activate virtyalenv ${VIRTUAL_ENV_NAME} local -> pyenv activate $VIRTUAL_ENV_NAME"
#pyenv activate $VIRTUAL_ENV_NAME

# ***********************
#  CONFIG pyenv-virtualenv
# ***********************

#python -m virtualenv | grep -q 'No module named' && pip install virtualenv || echo 'Virtualenv is installed'

#virtualenv $VIRTUAL_ENV_LOCAL
#source venv/bin/activate

# ***********************
#  CONFIG dependencies
# ***********************

echo
echo "*** CONFIG dependencies ***"

echo "* Upgrading pip" 
pip install --upgrade pip

python -m pre-commit | grep -q 'No module named' && pip install pre-commit || echo '* pre-commit is installed'

pip install -r requirements.txt

python -m pytest | grep -q 'No module named' && pip install pytest || echo '* pytest is installed'

pip install -r requirements-test.txt

# pip install -r requirements-doc.txt

# ***********************
#  CONFIG setup
# ***********************

mv setup/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push

# ***********************
#  CONFIG README.md
# ***********************

#rm README.md

#mv setup/Readme-template.md README.md

#rm -rf setup-folder

#cp .env.example .env