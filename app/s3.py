import logging
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

def create_bucket(bucket_name, region=None):
    try:
        s3_client = boto3.client('s3',
                      endpoint_url="http://localhost:4572",
                      use_ssl=False,
                      aws_access_key_id="test",
                      aws_secret_access_key="test",
                      region_name=region) 
        response = s3_client.list_buckets()
        found = False
        for bucket in response['Buckets']:
            if bucket_name == bucket["Name"]:
                found = True
        if not found:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if create_bucket("testbucket","ap-southeast-2"):
    logging.info("testbucket created")
else:
    logging.error("failed creating testbucket")