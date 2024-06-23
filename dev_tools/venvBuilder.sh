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
    while true; do
        read -p "Do you want to activate the virtual environment? (y/n): " activate_venv
        case $activate_venv in
            [Yy]* ) source venv/bin/activate; break;;
            [Nn]* ) echo "Exiting without activating the virtual environment."; exit;;
            * ) echo "Please answer yes (y) or no (n).";;
        esac
    done
    exit
fi

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Ask user if they want to install the requirements
while true; do
    read -p "Do you want to install the requirements? (y/n): " install_requirements
    case $install_requirements in
        [Yy]* ) pip install -r requirements.txt; break;;
        [Nn]* ) echo "Requirements not installed."; break;;
        * ) echo "Please answer yes (y) or no (n).";;
    esac
done
