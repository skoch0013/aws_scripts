import argparse
from actions_s3 import put_to_bucket

parser = argparse.ArgumentParser()
parser.add_argument('--bucket_name', type=str, default='ksyu2')
parser.add_argument('--local_file', type=str, default='/Users/ksyu/testfile')
parser.add_argument('--destination_file', type=str, default='testfile')
args = parser.parse_args()

if __name__ == "__main__":
    put_to_bucket(
        args.bucket_name, args.local_file, args.destination_file
    )