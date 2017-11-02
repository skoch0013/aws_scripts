import argparse
from actions_ec2 import create_instance

parser = argparse.ArgumentParser()
parser.add_argument('--image_id', type=str, default='ami-10547475') #ubuntu 16.04
parser.add_argument('--instance_type', type=str, default='t2.micro')
parser.add_argument('--key_name', type=str, default='ksyu')
parser.add_argument('--security_groups', type=str, default='sg-bf4e24d7')
parser.add_argument('--subnet_id', type=str, default='subnet-bc421bd5')
parser.add_argument('--tag_name', type=str, default='name')
parser.add_argument('--tag_value', type=str, default='ksyu_test')
# parser.add_argument('--iam_profile', type=str, default='')
args = parser.parse_args()

if __name__ == "__main__":
    create_instance(
        args.image_id, args.instance_type, args.key_name, args.security_groups, args.subnet_id, args.tag_name, args.tag_value
    )
