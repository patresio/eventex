#!/bin/bash

# Create a virtual environment
#echo "Creating a virtual environment..."
#python3.9 -m venv venv
#source venv/bin/activate

# Install the latest version of pip
echo "Installing the latest version of pip..."
python3 -m pip install --upgrade pip

# Upgrade SetupTools
python3 -m pip install --upgrade setuptools

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt
export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`

# Make migrations
echo "Making migrations..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

# Carrega Keynotes
python3 manage.py loaddata keynotes.json