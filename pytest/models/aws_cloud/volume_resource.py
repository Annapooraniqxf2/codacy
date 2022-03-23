"""
This python file helps to read the ec2 volume information from AWS using boto3

"""


import boto3
from abc import ABC, abstractmethod


class VolumeResource(ABC):
    """This class is used to fetch details of ec2 instance using boto3"""
    def __init__(self) -> None:
        self.ec2_volume_service = boto3.resource('ec2')
        

    @abstractmethod
    def fetch_volume_info():
        pass