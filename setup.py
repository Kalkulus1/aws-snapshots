from setuptools import setup

setup(
    name="aws_shots",
    version="1.0",
    author="Mumuni Mohammed",
    author_email="mumunim10@gmail.com",
    description="AWS_shots is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['aws_shots'],
    url="https://github.com/Kalkulus1/aws-snapshots",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        aws_shots=aws_shots.aws_shots:cli
    ''',
)