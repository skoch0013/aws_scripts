import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--instance_id', type=str, default='i-08b33871bac7763a0')
args = parser.parse_args()

ec2 = boto3.resource('ec2')
instance = ec2.instances.filter(InstanceIds=[args.instance_id]).terminate()

print instance