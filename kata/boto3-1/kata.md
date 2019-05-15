# Boto3 Kata 1

* Install awscli
* boto3 clients 

## Install awscli

1. Install awscli on your system using google for directions
2. Configure your default profile, this will require [aws-adfs](https://github.com/venth/aws-adfs)
3. Test awscli by running `aws s3 ls`

## boto3 clients and sessions

1. Create a python script `boto_test.py`, install and import boto3
2. Define a boto3 ec2 client
3. Store the output of a describe_instances api call and print it to the screen. (Hint use pprint for clean output of json.)
4. Use aws-adfs to define a second and different profile than above in challenge 1.2
5. Create a boto3 Sessions using the new profile, create a s3 client from the session
6. Use the s3 client to save all the buckets to a variable and print them to the screen.

## Paginating Results

1. Define a boto3 ec2 client for the nse-sandbox account
2. Use that client to query all the AMIs, print the total number ( Hint: describe_images(Owners=['self']) )
3. Create a ssm client and use `get_parameters_by_path(Path='/', Recursive=True)` to store all parameters, print the total number of parameters.
4. Now create a paginator that does the same but collects all ssm parameters