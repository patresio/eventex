#!/bin/bash

# Create a virtual environment
echo "Creating a virtual environment..."
python3.9 -m venv .venv
source .venv/bin/activate

# Install the latest version of pip
echo "Installing the latest version of pip..."
python -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python -m pip install -r requirements.txt

# Arrumando o urllib
python -m pip install --upgrade urllib3==1.26.15

# Make migrations
echo "Making migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --upload-unhashed-files

# Carrega Keynotes
#python manage.py loaddata keynotes.json