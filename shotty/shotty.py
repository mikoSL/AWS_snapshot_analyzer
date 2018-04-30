import boto3
import sys
import click

#use shotty profile in this session
session = boto3.Session(profile_name = 'shotty')
#get ec2
ec2 = session.resource('ec2')

#fun to list all EC2 instances
@click.command()
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(','.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return

if __name__ == '__main__':
    print(sys.argv)
    list_instances()
