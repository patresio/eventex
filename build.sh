#!/bin/bash

# Create a virtual environment
#echo "Creating a virtual environment..."
python3.9 -m venv venv
source venv/bin/activate


echo "Exportando as configurações na mão"
echo "Exportando as configurações na mão"
echo "Exportando as configurações na mão"
echo "Exportando as configurações na mão"
export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`


# Upgrade SetupTools
# Install the latest version of pip
python -m pip install wheel setuptools pip --upgrade

# Build the project
echo "Building the project..."
python -m pip install -r requirements.txt --no-cache-dir

# Make migrations
echo "Making migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Carrega Keynotes
echo "Load data keynotes Speakers ..."
python manage.py loaddata keynotes.json