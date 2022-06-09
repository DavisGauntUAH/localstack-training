import json
import logging
import boto3
from botocore.exceptions import ClientError
import os

AWS_REGION = 'us-east-1'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = 'http://localhost:4566'

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)
s3_client = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)
s3_resource = boto3.resource("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)


def create_bucket(bucket_name):
    
    try:
        resp = s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as err:
        logger.exception(f'Unable to create  S3 bucket locally. Error : {err}')
    else: return resp
    
    
def empty_bucket(b_name):
    
    try:
        bucket = s3_resource.Bucket(b_name)
        resp = bucket.objects.all().delete()
    except Exception as err:
        logger.exception(f'Error : {err}')
        raise
    
    
def del_bucket(b_name):
    
    try:
        empty_bucket(b_name)
        resp = s3_client.delete_bucket(Bucket=b_name)
    except ClientError as err:
        logger.exception(f'Error: could not delete bucket: {err}')
    else:
        return resp


def main():
    
    b_name = 'davis-test-bucket'
    
    logger.info('Creating S3 bucket on localy ...')
    s3_log = create_bucket(b_name)
    logger.info(json.dumps(s3_log, indent=4)+ '\n')
    del_bucket(b_name)
    pass


if __name__ == '__main__':
    main()