# About
manage EC2 instance snapshot with boto3.

## Configuration
using AWS CLI to create shotty configuration file

'aws configure --profile shotty'

## Running

'pipenv run python shotty/shotty.py <command>
<subcommand> <--project=PROJECT>'

* command * is instances, volumes, or snapshots.
* subcommand * -- depends on command
* project * is optional
