# ANSI escape codes for colored text
GREEN = "\033[92m"
RESET = "\033[0m"
RED = "\033[91m"
BLUE = "\033[94m"

print(GREEN + "Welcome to the AWS IP Prefix Finder!" + RESET)
print(GREEN + "This script will help you find and manage AWS-specific IP prefixes within your EC2 instance." + RESET)
print(GREEN + "Made with love by akshayh636" + RESET)
print(GREEN + "Make sure to support and follow (:" + RESET)

import boto3
import time

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
        
        # Display the current IP address
        if public_ip:
            print(BLUE + "Current IP address of the instance: " + public_ip + RESET)
        else:
            print(GREEN + "The instance currently has no public IP assigned." + RESET)

        # Check if the public IP matches the desired prefix
        if public_ip and public_ip.startswith(ip_prefix):
            print(GREEN + "Found a matching IP address: " + public_ip + RESET)
            break  # Exit the loop once we find a match

        print(GREEN + "No match yet, continuing the search..." + RESET)

        # Manage instance state based on the public IP
        if not public_ip:
            print(GREEN + "Starting the instance as it is currently stopped." + RESET)
            ec2.start_instances(InstanceIds=[instance_id])
            time.sleep(90)  # Wait for the instance to start
        else:
            print(GREEN + "Stopping the instance as it is currently running with a non-matching IP." + RESET)
            ec2.stop_instances(InstanceIds=[instance_id])
            time.sleep(90)  # Wait for the instance to stop
            
    except Exception as e:
        print(RED + "Error occurred: " + str(e) + RESET)
        print(RED + "Restarting the script in 5 seconds..." + RESET)
        time.sleep(5)  # Wait before restarting the script
        continue  # Restart the loop if an error occurs
