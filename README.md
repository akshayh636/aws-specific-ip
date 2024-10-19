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

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/akshayh636/aws-specific-ip/blob/main/config.py
    sudo python3 config.py
    ```