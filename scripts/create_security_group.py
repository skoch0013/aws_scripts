import argparse
from actions import create_security_group

parser = argparse.ArgumentParser()
parser.add_argument('--security_group_name', type=str, default='test1')
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

args = parser.parse_args()

if __name__ == "__main__":
    create_security_group(args.security_group_name, args.description, args.vpc_id, args.ingress, args.egress)