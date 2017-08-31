import argparse
import time
from actions import create_volume, attach_volume

parser = argparse.ArgumentParser()
parser.add_argument('--availability_zone', type=str, default='us-east-2a')
parser.add_argument('--size', type=int, default=2) #gb
parser.add_argument('--snapshot_id', type=str, default='snap-079ac1f64366bc5b2')
parser.add_argument('--instance_id', type=str, default='i-0b90d938d2d103adc')
parser.add_argument('--device', type=str, default='/dev/sdj')

args = parser.parse_args()
# az = us-east-2a

ebs = create_volume(args.availability_zone, args.size, args.snapshot_id)
time.sleep(10)
attach_volume(args.instance_id, ebs.id, args.device)

