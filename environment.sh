#!/bin/bash

# Check if the script is run as root or with sudo
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or with sudo."
    exit 1
fi

# Function to handle command execution and error checking
execute_command() {
    $1 &>/dev/null
    if [ $? -ne 0 ]; then
        echo "Error: $2. Exiting..."
        exit 1
    fi
}

# Install pip
echo "Installing pip..."
execute_command "sudo apt update" "Failed to update package list"
execute_command "sudo apt install -y python3-pip" "Failed to install pip"

# Environment setup
echo "Setting up the environment..."
execute_command "sudo apt install -y build-essential libssl-dev libffi-dev python3-dev python3-venv" "Failed to install development packages"

# Create a directory for virtual environments
mkdir -p ~/environments
cd ~/environments

# Create and start the virtual Python environment
echo "Starting the virtual Python environment..."
execute_command "python3 -m venv akshay" "Failed to create the virtual environment"

source akshay/bin/activate

echo "Python environment setup is successful."
