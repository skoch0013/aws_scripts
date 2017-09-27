import argparse
from actions_ec2 import create_security_group

parser = argparse.ArgumentParser()
parser.add_argument('--security_group_name', type=str, default='test33')
parser.add_argument('--description', type=str, default='test_sg_allow_ssh')
parser.add_argument('--vpc_id', type=str, default='vpc-6889c001')
parser.add_argument('--ingress', type=str, default=
[{
    "IpProtocol": "tcp", "IpRanges": [{"CidrIp": "0.0.0.0/0"}], "FromPort":22, "ToPort":22
  },
  {
    "IpProtocol": "tcp", "IpRanges": [{"CidrIp": "0.0.0.0/0"}], "FromPort":80, "ToPort":80
  },
  {
    "IpProtocol": "icmp", "IpRanges": [{"CidrIp": "0.0.0.0/0"}], "FromPort":-1, "ToPort":-1
  }
])
parser.add_argument('--egress', type=str, default=[])
parser.add_argument('--tag_name', type=str, default='name')
parser.add_argument('--tag_value', type=str, default='ksyu_test')

args = parser.parse_args()

if __name__ == "__main__":
    create_security_group(
        args.security_group_name, args.description, args.vpc_id, args.ingress, args.egress, args.tag_name, args.tag_value
    )