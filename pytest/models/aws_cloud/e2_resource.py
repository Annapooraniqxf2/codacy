"""
This python file helps to read the ec2 instance information from AWS using boto3

"""


import boto3
from abc import ABC, abstractmethod


class Ec2(ABC):
    """This class is used to fetch details of ec2 instance using boto3"""
    def __init__(self) -> None:
        self.ec2_service = boto3.client('ec2')
        

    @abstractmethod
    def fetch_instance_info():
        pass
   