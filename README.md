# AWS-Specific-IP in VM

This repository contains a script designed to find and manage AWS-specific IP prefixes within a virtual machine (VM). Whether you need to locate specific IP ranges for compliance, security, or network management purposes, this tool offers a straightforward solution with the help of [boto3](https://github.com/boto/boto3) 

## Features

- **IP Prefix Search**: Quickly find specific AWS IP prefixes within your VM.
- **Flexible Filtering**: Apply filters to narrow down IP prefix searches based on your criteria.
- **Detailed Reporting**: Generate detailed reports of IP prefix findings.
- **Easy Integration**: Integrate the script into existing VM management workflows.
- **Automation Ready**: Script can be used in automation pipelines for dynamic IP management.

## Getting Started

### Prerequisites

- An AWS account with access to relevant services.
- A virtual machine instance running on AWS.
- AWS CLI configured with your AWS credentials.
- AWS VM instance id and region

### Making up the enviroment

1. Clone the Repository

   ```bash
    wget https://raw.githubusercontent.com/akshayh636/aws-specific-ip/main/environment.sh
    ```
2. Make the Script Executable  
    ```bash
    chmod +x environment.sh
    ```
3. Run the Script 
    ```bash
    sudo ./environment.sh
    ```

### To start the environment , run this
   ```bash
cd ~/environments/akshay
source bin/activate
  ```
### So the environment is ready to run the script 
1. Install boto3
    
```bash
pip install boto3
  ```
2. Clone the python script

```bash
wget https://raw.githubusercontent.com/akshayh636/aws-specific-ip/main/aws_ip.py
  ```
3. Run the Script and enter your aws credentials and your preferable ip prefix

```bash
python3 aws_ip.py
  ```
