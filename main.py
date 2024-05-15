import boto3
from botocore.exceptions import ClientError
import sys

def get_secret():
    region_name = "ap-southeast-1"

    # Retrieve the first arg
    if len(sys.argv) > 1:
        secret_name = sys.argv[1]
    else:
        print("Please add secret name to retrieve.")
        exit()

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Correctly access the secret value from the response
    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
    else:
        secret = get_secret_value_response['SecretBinary']

    print(secret)  # Print the secret value to verify

    # Your code goes here.

get_secret()