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
sudo apt update &>/dev/null
sudo apt install -y python3-pip &>/dev/null

if [ $? -ne 0 ]; then
    echo "Failed to install pip. Exiting..."
    exit 1
fi

# Environment setup
echo "Setting up the environment..."
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev python3-venv &>/dev/null

if [ $? -ne 0 ]; then
    echo "Failed to install development packages. Exiting..."
    exit 1
fi

# Create and start the virtual Python environment
echo "Creating the virtual environment directory..."
# Create the akshay directory in the home folder with root access
sudo mkdir -p ~/akshay
# Create the virtual environment inside the akshay folder
python3 -m venv ~/akshay &>/dev/null

if [ $? -ne 0 ]; then
    echo "Failed to create the virtual environment. Exiting..."
    exit 1
fi

# Change permissions of the virtual environment folder
sudo chown -R $(whoami):$(whoami) ~/akshay
sudo chmod -R 775 ~/akshay

# Provide instructions for the user to manually activate the environment
echo -e "${GREEN}To activate the virtual environment, run the following commands:${NC}"
echo -e "${GREEN}source akshay/bin/activate${NC}"

echo "Python environment setup is successful."
