import boto3
import time
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')


def create_volume(availability_zone, size, snapshot_id):
    ebs = ec2.create_volume(
        AvailabilityZone=availability_zone,
        Size=size,
        SnapshotId=snapshot_id
    )
    return ebs


def attach_volume(instance_id, volume_id, device):
    res = ec2.Instance(instance_id)
    res.attach_volume(
        VolumeId=volume_id,
        Device=device
    )
    print res


def create_instance(image_id, instance_type, key_name, security_groups, subnet_id):
    instance = ec2.create_instances(
    ImageId=image_id,
    MinCount=1,
    MaxCount=1,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=[security_groups],
    SubnetId=subnet_id
    )
    for i in instance:
        return i


def list_instances():
    for instance in ec2.instances.all():
        print instance.id, instance.state


def terminate_instance(instance_id):
    instance = ec2.instances.filter(
        InstanceIds=[instance_id]
    ).terminate()
    print instance


def terminate_all_running_instances():
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}]
    )
    for instance in instances:
        instance.terminate()
        print(instance.id, instance.instance_type)


def get_volume_id(instance_id):
    inst = ec2.Instance(instance_id)
    volumes = inst.volumes.all()
    for v in volumes:
        return v


def create_snapshot(volume_id):
    snapshot = ec2.create_snapshot(
        VolumeId=volume_id,
        Description="test")
    return snapshot


def create_security_group(security_group_name, description, vpc_id, inbound_rules, outbound_rules):
    group = ec2.create_security_group(
        GroupName=security_group_name,
        Description=description,
        VpcId=vpc_id)
    time.sleep(10)

    try:
        for rule in inbound_rules:
            group.authorize_ingress(
                IpPermissions=[rule]
            )
        for rule in outbound_rules:
            group.authorize_egress(
                IpPermissions=[rule]
            )
    except ClientError as e:
        print(e)
    return group