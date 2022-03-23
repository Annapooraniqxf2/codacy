"""
Conftest fixtures for ec2, network and volume

"""

import os
import sys
import yaml
from yaml.loader import SafeLoader
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from checks.aws_cloud.aws_ec2 import Check
from checks.aws_cloud.network_check import NetworkCheck
from checks.aws_cloud.volume_check import VolumeCheck
from fixtures.aws_cloud.ec2 import Ec2Info
from fixtures.aws_cloud.network_interface import Network
from fixtures.aws_cloud.volume import Volume


TAGS = [{'Name': 'tag:Name','Values': ['onboarding_qa_annapoorani']}]
INTERFACE_ID = 'eni-06f775397d13d8b69'



@pytest.fixture
def read_yaml() -> list:
    """Read the test_data.yaml file"""
    test_data_file = "tests/aws_cloud/test_data.yaml"
    with open (test_data_file) as test_file:
        data = yaml.load(test_file, Loader=SafeLoader)

    return data


@pytest.fixture
def get_instance_information() -> list:
    """Get the instance information from AWS"""

    ec2_info = Ec2Info(TAGS)
    instance_info = ec2_info.fetch_instance_info()

    return  instance_info


@pytest.fixture
def ec2_object() -> object:
    """ Create the ec2 object"""
    aws_ec2_object = Check()

    return  aws_ec2_object


@pytest.fixture
def get_volume_information() -> list:
    """Get the instance information from AWS"""
    volume_info = Volume(TAGS)
    instance_volume_info = volume_info.fetch_volume_info()

    return  instance_volume_info


@pytest.fixture
def volume_object() -> object:
    """Create the volume object"""
    ec2_volume_object = VolumeCheck()

    return  ec2_volume_object


@pytest.fixture
def get_network_information() -> object:
    """Get the network information from the AWS"""
    network_info = Network(INTERFACE_ID)
    instance_network_info = network_info.fetch_network_info()

    return instance_network_info


@pytest.fixture
def network_object() -> object:
    """Create the network object"""
    ec2_network_object = NetworkCheck()

    return  ec2_network_object
