import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--image_id', type=str, default='ami-ea87a78f')
parser.add_argument('--instance_type', type=str, default='t2.micro')
parser.add_argument('--key_name', type=str, default='ksyu')
# parser.add_argument('--security_groups', type=str, default='')
parser.add_argument('--subnet_id', type=str, default='subnet-bc421bd5')
# parser.add_argument('--iam_profile', type=str, default='')
args = parser.parse_args()

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId=args.image_id,
    MinCount=1,
    MaxCount=1,
    InstanceType=args.instance_type,
    KeyName=args.key_name,
    SubnetId=args.subnet_id
)
for i in instance:
    print(i.id, i.instance_type)