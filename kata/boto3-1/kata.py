# ## boto3 clients and sessions

# 1. Create a python script `boto_test.py`, install and import boto3
# 2. Define a boto3 ec2 client
# 3. Store the output of a describe_instances api call and print it to the screen. (Hint use pprint for clean output of json.)
# 4. Use aws-adfs to define a second and different profile than above in challenge 1.2
# 5. Create a boto3 Sessions using the new profile, create a s3 client from the session
# 6. Use the s3 client to save all the buckets to a variable and print them to the screen.

# 1.
import boto3

# 2.
my_ec2_client = boto3.client('ec2')

# 3.
from pprint import pprint
instance_descriptions = my_ec2_client.describe_instances()
pprint(instance_descriptions)

# 5.
nsetool_dev_session = boto3.Session(profile_name="nsetool-dev")
nsetool_dev_s3_client = nsetool_dev_session.client('s3')

# 6.
response = nsetool_dev_s3_client.list_buckets()
bucket_list = response['Buckets']
for bucket in bucket_list:
    print(bucket['Name'])

# ## Pagenating Results

# 1. Define a boto3 ec2 client for the nse-sandbox account
# 2. Use that client to query all the AMIs, print the total number ( Hint: describe_images(Owners=['self']) )
# 3. Create a ssm client and use `get_parameters_by_path(Path='/', Recursive=True)` to store all parameters, print the total number of parameters.
# 4. Now create a paginator that does the same but collects all ssm parameters

# 1.
session = boto3.Session(profile_name="nsetool-sbx")
ec2_client = session.client('ec2')

# 2.
images = ec2_client.describe_images(Owners=['self'])
print(len(images['Images']))

# 3.
ssm_client = session.client('ssm')
response = ssm_client.get_parameters_by_path(Path='/', Recursive=True)
print(len(response['Parameters']))

# 4.
paginator = ssm_client.get_paginator('get_parameters_by_path')
response_iterator = paginator.paginate(Path='/', Recursive=True)

all_parameters = []
for response in response_iterator:
    all_parameters = all_parameters + response['Parameters']
    print(page['Contents'])

pprint(all_parameters)