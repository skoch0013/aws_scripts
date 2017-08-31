import argparse
import time
from actions import *

parser = argparse.ArgumentParser()
parser.add_argument('--image_id', type=str, default='ami-ea87a78f')
parser.add_argument('--instance_type', type=str, default='t2.micro')
parser.add_argument('--key_name', type=str, default='ksyu')
# parser.add_argument('--security_groups', type=str, default='')
parser.add_argument('--subnet_id', type=str, default='subnet-bc421bd5')
# parser.add_argument('--iam_profile', type=str, default='')
#ebs
parser.add_argument('--availability_zone', type=str, default='us-east-2a')
parser.add_argument('--size', type=int, default=2) #gb
parser.add_argument('--device', type=str, default='/dev/sdj')
parser.add_argument('--snapshot_id', type=str, default='snap-079ac1f64366bc5b2')

args = parser.parse_args()

#create instance
instance = create_instance(args.image_id, args.instance_type, args.key_name, args.subnet_id)
instance.wait_until_running()

#create & attach volume
ebs = create_volume(args.availability_zone, args.size, args.snapshot_id)
time.sleep(10)
attach_volume(instance.id, ebs.id, args.device)