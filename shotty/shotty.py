import boto3

if __name__ == '__main__':
    #use shotty profile in this session
    session = boto3.Session(profile_name = 'shotty')

    #get ec2
    ec2 = session.resource('ec2')

    #list all instances
    for i in ec2.instances.all():
        print(i)
