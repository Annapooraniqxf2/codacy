""" 
This module collects ec2 instance volume info from aws using boto3

"""

from  models.aws_cloud.volume_resource import VolumeResource


class Volume(VolumeResource):
    """Fetch the instance volume info using the ec2 service"""

    def __init__(self, tags) -> None:
        super().__init__()
        self.tags = tags
        
    
    def fetch_volume_info(self) -> list:
        """Fetch the ebs volume from the available instances"""
        try:
            self.ebs_response = self.ec2_volume_service.volumes.filter(Filters=self.tags)
            all_ebs_list = []
            if self.ebs_response:
                for volume in self.ebs_response:
                    all_ebs_dict = {}
                    all_ebs_dict.update(instance_volume_id=volume.id,
                                instance_voulme_size=volume.size,
                                instance_volume_state=volume.state)
                    all_ebs_list.append(all_ebs_dict)
        except Exception as e:
            print(e)
            print("The instance volume object doesnt exist")

        return all_ebs_list   
