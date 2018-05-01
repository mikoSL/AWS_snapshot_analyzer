import boto3
import click

#use shotty profile in this session
session = boto3.Session(profile_name = 'shotty')
ec2 = session.resource('ec2')

#function to filter list_instances
def filter_instances(project):
    instances =[]

    if project:
        filters = [{'Name':'tag:project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances

@click.group()
def instances():
    """commands for instances"""

@instances.command('list')
@click.option('--project', default=None,
    help = 'Only instances for project (tag Project:<name> )')

#function to list all EC2 instances
def list_instances(project):
    "List EC2 instances"

    instances = filter_instances(project)
    for i in instances:
        tags = { t['Key']:t['Value'] for t in i.tags or []}
        print(','.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('project','<no project>')
            )))
    return

# stop instances
@instances.command('stop')
@click.option('--project', default=None,
    help='Only instances for project')

def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instances(project)
    for i in instances:
        print('Stoping {0}...'.format(i.id))
        i.stop()

    return

# start instances
@instances.command('start')
@click.option('--project', default=None,
    help='Only instances for project')

def start_instances(project):
    "Start EC2 instances"

    instances = filter_instances(project)
    for i in instances:
        print('Starting {0}...'.format(i.id))
        i.stop()

    return

if __name__  == '__main__':
    instances()
