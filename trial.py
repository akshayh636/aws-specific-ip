
import boto3
import time

# Set your AWS access key and secret key
aws_access_key = 'AKIA4SZHN6E3IXXUMFUG'
aws_secret_key = 'cEtDaQXwFAkoSKtuzEzKpRgY7z+yNqc+yY3egiNE'

# Set the region and instance ID of your AWS EC2 instance
region = 'ap-south-1'  # Change this to the appropriate region
instance_id = 'i-07f5c02acfdaa922c'

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

while True:
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        public_ip = instance.get('PublicIpAddress')

        if public_ip and (
            public_ip.startswith('43.205.230') or public_ip.startswith('43.205.155') or 
            public_ip.startswith('43.205.140') or public_ip.startswith('43.205.115') or 
            public_ip.startswith('43.205.143') or public_ip.startswith('43.205.239') or 
            public_ip.startswith('43.205.99') or public_ip.startswith('43.205.233') or 
            public_ip.startswith('43.205.116') or public_ip.startswith('43.205.209') or 
            public_ip.startswith('43.205.119') or public_ip.startswith('43.205.203') or 
            public_ip.startswith('43.205.146') or public_ip.startswith('43.205.216') or 
            public_ip.startswith('43.205.254') or public_ip.startswith('43.205.117') or 
            public_ip.startswith('43.205.98') or public_ip.startswith('43.205.211') or 
            public_ip.startswith('43.205.138') or public_ip.startswith('43.205.196') or 
            public_ip.startswith('43.205.214') or public_ip.startswith('43.205.195') or 
            public_ip.startswith('43.205.243') or public_ip.startswith('43.205.242') or 
            public_ip.startswith('43.205.255') or public_ip.startswith('43.205.242') or 
            public_ip.startswith('43.205.127') or public_ip.startswith('43.205.114') or 
            public_ip.startswith('43.205.236') or public_ip.startswith('43.205.196') or 
            public_ip.startswith('43.205.242') or public_ip.startswith('43.205.112') or 
            public_ip.startswith('43.205.112') or public_ip.startswith('43.205.231') or 
            public_ip.startswith('43.205.198') or public_ip.startswith('43.205.199') or 
            public_ip.startswith('43.205.128') or public_ip.startswith('43.205.235') or 
            public_ip.startswith('43.205.139') or public_ip.startswith('43.205.212') or 
            public_ip.startswith('43.205.145') or public_ip.startswith('43.205.240') or 
            public_ip.startswith('43.205.229') or public_ip.startswith('43.205.96') or 
            public_ip.startswith('43.205.118') or public_ip.startswith('43.205.144') or 
            public_ip.startswith('43.205.206') or public_ip.startswith('43.205.241') or 
            public_ip.startswith('43.205.237') or public_ip.startswith('43.205.136') or 
            public_ip.startswith('43.205.177') or public_ip.startswith('43.205.103') or 
            public_ip.startswith('43.205.237')
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
