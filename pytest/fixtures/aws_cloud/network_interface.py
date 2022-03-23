""" 
This module collects ec2 instance network info from aws using boto3

"""


from  models.aws_cloud.network_resource import NetworkResource

class Network(NetworkResource):
    """Fetch the instance network interface info using the ec2 service"""

    def __init__(self, id) -> None:
        super().__init__()
        self.id = id
        
    
    def fetch_network_info(self) -> object:
        """Fetch the network information for the available instances"""
        self.network_response = self.ec2_network_service.NetworkInterface(self.id)

        return self.network_response        