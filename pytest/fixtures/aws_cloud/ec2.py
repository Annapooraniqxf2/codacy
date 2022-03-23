""" 
This module collects ec2 instance info from aws using boto3

"""

from  models.aws_cloud.e2_resource import Ec2


class Ec2Info(Ec2):
    """Fetch the instance info using the ec2 service"""
    def __init__(self, tags) -> None:
        super().__init__()
        self.tags = tags
    
    def fetch_instance_info(self) -> list:
        """Fetch the tag name and values for the available instances"""
        try:
            self.response = self.ec2_service.describe_instances(Filters=self.tags).get('Reservations')
            all_tags_list = []
            if self.response:
                for each_reservation in self.response:
                    for each_instance in each_reservation['Instances']:
                        all_tags_dict = {}
                        all_tags_dict.update(instance_image_id=each_instance['ImageId'],
                        instance_securtity_groups=each_instance['SecurityGroups'],
                        instance_state=each_instance['State'],
                        instance_public_address=each_instance['PublicIpAddress'],
                        instance_tag= each_instance['Tags'])
                    all_tags_list.append(all_tags_dict)
        except Exception as e:
            print(e)
            print("The instance object doesnt exist")

        return all_tags_list    
