# aws_shots
A project to manage AWS EC2 instance snapshots

## About

This project uses boto3 to manage AWS EC2 instance snapshots.

## Configuring 

aws_shots uses the configuration file created by the AWS CLI. e.g

`aws configure --profile aws_shots`

## Installation

Download *aws_shots-1.0-py3-none-any.whl* file and run:

`pip3 install aws_shots-1.0-py3-none-any.whl`

This is much easier for now.

Or you could clone the project and run the setup file.

`python setup.py install`

## Running

`aws_shots <command> <--project=PROJECT>`

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional

