import logging
import boto3

AWS_REGION = 'us-east-1'
LOCALSTACK_INTERNAL_ENDPOINT_URL = 'http://host.docker.internal:4566'

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')


def handler(event, context):
    
    s3_resorce = boto3.client('s3', region_name=AWS_REGION, 
                              endpoint_url=LOCALSTACK_INTERNAL_ENDPOINT_URL)

    pass