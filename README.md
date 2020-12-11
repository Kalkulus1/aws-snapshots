# aws_shots
A project to manage AWS EC2 instance snapshots

## About

This project uses boto3 to manage AWS EC2 instance snapshots.

## Configuring 

aws_shots uses the configuration file created by the AWS CLI. e.g

`aws configure --profile aws_shots`

## Running

`pipenv run python aws_shots/aws_shots.py <command> <--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional

