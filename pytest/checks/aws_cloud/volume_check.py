"""
This page checks the fetched ec2 network interface info against with test data

"""

class VolumeCheck:
    """Contains method to compare the ec2 volume data"""

    def compare_volume_id(self, instance_info, test_data) -> bool:
        """Compare the ec2 volume id"""
        result_flag = False
        expected_tag = instance_info['instance_volume_id']
        actual_tag = test_data['instance_volume_id']
        if expected_tag == actual_tag:
            result_flag = True

        return result_flag


    def compare_volume_size(self, instance_info, test_data) -> bool:
        """Compare the ec2 volume size"""
        result_flag = False
        expected_volume_size = instance_info['instance_voulme_size']
        actual_volume_size = test_data['instance_voulme_size']
        if expected_volume_size == actual_volume_size:
            result_flag = True

        return result_flag


    def compare_volume_state(self, instance_info, test_data) -> bool:
        """Compare the ec2 volume state"""
        result_flag = False
        expected_volume_state = instance_info['instance_volume_state']
        actual_volume_state = test_data['instance_volume_state']
        if expected_volume_state == actual_volume_state:
            result_flag = True

        return result_flag