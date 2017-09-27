import boto3
from botocore.exceptions import ClientError
from botocore.client import Config

s3 = boto3.resource('s3')

def create_bucket(bucket_name, tag_name, tag_value, region):
    s3_tag = {"Key": tag_name, "Value": tag_value}
    try:
        s3 = boto3.resource('s3', region_name='us-east-2', config=Config(signature_version='s3v4'))
        bucket = s3.create_bucket(Bucket=bucket_name
                                  ,CreateBucketConfiguration={'LocationConstraint': region}
                                  )
        tagging = bucket.Tagging()
        tagging.put(Tagging={'TagSet': [s3_tag]})
        tagging.reload()
        return bucket.name
    except ClientError as e:
        print(e)


def put_to_bucket(bucket_name, local_file, destination_file):
    try:
        s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
        with open(local_file, 'rb') as data:
            s3.upload_fileobj(data, bucket_name, destination_file)
        return True
    except ClientError as e:
        print(e)