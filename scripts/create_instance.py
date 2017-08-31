import argparse
from actions import create_instance

parser = argparse.ArgumentParser()
parser.add_argument('--image_id', type=str, default='ami-ea87a78f')
parser.add_argument('--instance_type', type=str, default='t2.micro')
parser.add_argument('--key_name', type=str, default='ksyu')
# parser.add_argument('--security_groups', type=str, default='')
parser.add_argument('--subnet_id', type=str, default='subnet-bc421bd5')
# parser.add_argument('--iam_profile', type=str, default='')

args = parser.parse_args()
create_instance(args.image_id, args.instance_type, args.key_name, args.subnet_id)
