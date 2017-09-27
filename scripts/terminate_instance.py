from actions_ec2 import terminate_instance
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--instance_id', type=str, default='i-01486cfdd5c2659da')
args = parser.parse_args()

if __name__ == "__main__":
    terminate_instance(args.instance_id)