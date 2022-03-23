"""
This python file helps to read the ec2 network information from AWS using boto3

"""


import boto3
from abc import ABC, abstractmethod


class NetworkResource(ABC):
    """This class is used to fetch details of ec2 instance using boto3"""
    def __init__(self) -> None:
        self.ec2_network_service = boto3.resource('ec2')
        

    @abstractmethod
    def fetch_network_info():
        pass