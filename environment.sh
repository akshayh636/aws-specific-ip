#!/bin/bash

# Define color codes
GREEN='\033[1;32m'
NC='\033[0m' # No Color

# Check if the script is run as root or with sudo
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or with sudo."
    exit 1
fi

# Install pip
echo "Installing pip..."
sudo apt update 
if ! sudo apt install -y python3-pip; then
    echo "Failed to install pip. Exiting..."
    exit 1
fi

# Environment setup
echo "Setting up the environment..."
if ! sudo apt install -y build-essential libssl-dev libffi-dev python3-dev python3-venv; then
    echo "Failed to install development packages. Exiting..."
    exit 1
fi

# Create and start the virtual Python environment
echo "Creating the virtual environment directory..."
mkdir akshay

if python3 -m venv ~/akshay; then
    echo -e "${GREEN}Virtual environment created successfully at ~/akshay.${NC}"
else
    echo "Failed to create the virtual environment. Check for errors above."
    exit 1
fi

# Change permissions of the virtual environment folder
echo "Changing permissions of the virtual environment directory..."
sudo chown -R $(whoami):$(whoami) ~/akshay
sudo chmod -R 775 ~/akshay

# Provide instructions for the user to manually activate the environment
echo -e "${GREEN}To activate the virtual environment, run the following command:${NC}"
echo -e "${GREEN}source ~/akshay/bin/activate${NC}"

echo "Python environment setup is successful."
