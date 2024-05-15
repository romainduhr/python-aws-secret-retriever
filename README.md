# Secret Retriever for aws secret

## Overview

This python code retrieve an encrypted aws secret using boto3 package

## Usage

You must have the following:

- Python3.6 or later
- pip (python package manager)

Install boto3:

```bash
pip install boto3
```

Install awscli:

```bash
sudo apt install awscli
```

Configure aws:

```bash
aws configure
```

Fill your information

Retrieve a secret

```bash
python3 main.py YOUR_SECRET_NAME
```
