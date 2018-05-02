from setuptools import setup

setup(
    name='AWS_snapshot_analyzer',
    version='0.1',
    description='a tool to manage ASW EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/mikoSL/AWS_snapshot_analyzer',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points={
        'console_scripts':[
            'shotty=shotty.shotty:cli'
        ],
    },

)
