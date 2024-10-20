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

# Create and start the virtual Python environment
echo "Installing the environment..."
python3 -m venv akshay &>/dev/null

if [ $? -ne 0 ]; then
    echo "Failed to create the virtual environment. Exiting..."
    exit 1
fi

# Starting the environments
echo -e "${GREEN}Python environment setup is successful.:${NC}"
echo -e "${GREEN}Starting the environment${NC}"
source akshay/bin/activate
