echo -e "${GREEN}AWS Ip Prefix Script"

echo -e "${GREEN}Made By https://github.com/akshayh636"

if [ `whoami` != root ]; then
	echo "ERROR: You need to run the script as user root or add sudo before command."
	exit 1
fi

#!/usr/bin/env python3

import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Check for Python 3
if sys.version_info[0] < 3:
    print("This script requires Python 3.")
    sys.exit(1)

# Try to import Boto3, and install it if it's not available
try:
    import boto3
except ImportError:
    print("Boto3 not found. Installing...")
    install('boto3')
    import boto3

import argparse
import time

# Prompt user for AWS credentials
aws_access_key_id = input("Enter your AWS Access Key ID: ")
aws_secret_access_key = input("Enter your AWS Secret Access Key: ")

# Set up Boto3 client with user-provided credentials
if aws_session_token:
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token
    )
else:
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )


# Set the region and instance ID of your AWS EC2 instance
region = input("Enter your vm region: ")
instance_id = input("Enter your instance id: ")

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


while True:
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        public_ip = instance.get('PublicIpAddress')

        if public_ip and (public_ip.startswith('43.205'
        ):
            # Stop the instance and restart the search
            print("Stopping")
            ec2.stop_instances(InstanceIds=[instance_id])
            time.sleep(90)  # Wait for the instance to stop (adjust as needed)
            ec2.start_instances(InstanceIds=[instance_id])
            print("stopped and restarted.")
            continue
        elif public_ip and public_ip.startswith('43.205'):
            print("Found matching IP")
            # Restart the loop to continue searching
            break
        else:
            print("Searching")
            # Choose whether to start or stop the instance
            if public_ip is None:
                # Start the instance if it's not running
                ec2.start_instances(InstanceIds=[instance_id])
            else:
                # Stop the instance if it's running
                ec2.stop_instances(InstanceIds=[instance_id])

            # Sleep for a while to avoid excessive API requests
            time.sleep(30)
            
    except Exception as e:
        print("Error occurred", e)
        print("Restarting the script...")
        time.sleep(5)  # Wait for 5 seconds before restarting the script
        continue  # Restart the loop if an error occurs
