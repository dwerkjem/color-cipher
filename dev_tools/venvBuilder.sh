#!/usr/bin/env bash

# This script is used to create a virtual environment for the project

# Check if the venv module is installed
if ! python3 -c "import venv" &> /dev/null
then
    echo "The venv module is not installed"
    exit
fi

# Check if the venv directory exists
if [ -d "venv" ]
then
    echo "venv directory already exists"
    exit
fi

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# ask user if they want to install the requirements
read -p "Do you want to install the requirements? (y/n): " install_requirements

if [ "$install_requirements" == "y" ]
then
    # Install the requirements
    pip install -r requirements.txt
fi