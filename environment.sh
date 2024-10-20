#!/bin/bash

# Check if the script is run as root or with sudo
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or with sudo."
    exit 1
fi

# Install pip
echo "Installing pip..."
sudo apt update
sudo apt install -y python3-pip

if [ $? -ne 0 ]; then
    echo "Failed to install pip. Exiting..."
    exit 1
fi

# Environment setup
echo "Setting up the environment..."
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev python3-venv

if [ $? -ne 0 ]; then
    echo "Failed to install development packages. Exiting..."
    exit 1
fi

# Create a directory for virtual environments
mkdir environments
cd environments

# Create and start the virtual Python environment
echo "Starting the virtual Python environment..."
python3 -m venv akshay

if [ $? -ne 0 ]; then
    echo "Failed to create the virtual environment. Exiting..."
    exit 1
fi

source akshay/bin/activate

if [ $? -ne 0 ]; then
    echo "Failed to activate the virtual environment. Exiting..."
    exit 1
fi

echo "Python environment setup is successful."
