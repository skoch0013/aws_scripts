import argparse
from actions_s3 import create_bucket

parser = argparse.ArgumentParser()
parser.add_argument('--bucket_name', type=str, default='ksyu2')
parser.add_argument('--tag_name', type=str, default='name')
parser.add_argument('--tag_value', type=str, default='ksyu_test')
parser.add_argument('--region', type=str, default='us-east-2')
args = parser.parse_args()

if __name__ == "__main__":
    create_bucket(
        args.bucket_name, args.tag_name, args.tag_value, args.region
    )