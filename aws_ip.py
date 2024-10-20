# ANSI escape codes for green text
GREEN = "\033[92m"
RESET = "\033[0m"

print(GREEN + "Welcome to the AWS IP Prefix Finder!" + RESET)
print(GREEN + "This script will help you find and manage AWS-specific IP prefixes within your EC2 instance." + RESET)
print(GREEN + "Made with love by akshayh636" + RESET)
print(GREEN + "Make sure to support and follow (:" + RESET)


import boto3
import time
import subprocess
import sys

# Prompt the user for AWS credentials and instance details
aws_access_key = input(GREEN + "Enter your AWS access key: " + RESET)
aws_secret_key = input(GREEN + "Enter your AWS secret key: " + RESET)
region = input(GREEN + "Enter the AWS region: " + RESET)
instance_id = input(GREEN + "Enter the AWS EC2 instance ID: " + RESET)
ip_prefix = input(GREEN + "Enter the IP prefix to search for (e.g., 43.205): " + RESET)

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

while True:
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        public_ip = instance.get('PublicIpAddress')

        if public_ip and (
            public_ip.startswith('ip_prefix') 
        ):
            # Stop the instance and restart the search
            print("Stopping")
            ec2.stop_instances(InstanceIds=[instance_id])
            time.sleep(90)  # Wait for the instance to stop (adjust as needed)
            ec2.start_instances(InstanceIds=[instance_id])
            print("stopped and restarted.")
            continue
        elif public_ip and public_ip.startswith('ip_prefix'):
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
