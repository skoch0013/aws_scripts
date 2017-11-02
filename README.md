## About

This is an educational project, which contains aws scripts and ansible playbooks.

Scripts: ```scripts```

Playbooks: ```ansible```

### Prerequisites

You'll need to have pip installed:

```
sudo easy_install pip
```
ansible:

```
sudo pip install ansible 
```

as well as aws cli:

```
pip install awscli 
```
and boto3
```
pip install boto3 
```
Also, make sure aws cli is configured with your access keys:
```
aws configure
```

### AWS scripts

The scripts cover main vpc/ec2/s3 actions and can be run from either command line or IDE

Example:
```
python scripts/create_bucket.py --bucket_name=test --tag_name=test --tag_value=test --region=us-east-2
```

Scripts list:

```
#vpc&ec2
create_security_group.py
create_instance.py
create_attach_volume.py
list_instances.py
terminate_instance.py
terminate_all_running_instances.py
```
```
#s3
create_bucket.py
put_to_bucket.py
```
```
#all-in-one script to fire up SG+ instance + additional volume
all_in_one.py
```

## Ansible

### Setup /etc/ansible/hosts file 
with the hosts you'll be provisioning to:
```
[aws]
hostname or ips here 
```

### Run the playbook directly

```
ansible-playbook playbook.yml --private-key=key_location.pem
```

### Use ansible provisioner with Vagrant:
add the following in the Vagrantfile:
```
# Provisioning configuration for Ansible.
config.vm.provision "ansible" do |ansible|
ansible.playbook = "playbook.yml"
end
```

## Authors

* **Oksana** - *Initial work* - [hey!](https://www.linkedin.com/in/oivasenko/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

