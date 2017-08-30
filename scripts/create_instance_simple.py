import boto3

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-ea87a78f',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='ksyu',
    SubnetId='subnet-bc421bd5'
    )
print instance[0].id


