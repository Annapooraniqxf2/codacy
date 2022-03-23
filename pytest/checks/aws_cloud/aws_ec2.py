"""
This page checks the fetched ec2 info against with test data

"""

class Check:
    """ Checks the data"""    

    def compare_ec2_tags(self, instance_info, test_data) -> bool:
        """Compare the ec2 tags"""
        result_flag = False
        expected_tag = instance_info['instance_tag']
        actual_tag = test_data['instance_tag']
        if expected_tag == actual_tag:
            result_flag = True

        return result_flag        


    def compare_image_id(self, instance_info, test_data) -> bool:
        """Compare the image id"""
        expected_image_id = instance_info['instance_image_id']
        actual_image_id = test_data['instance_image_id']
        if expected_image_id == actual_image_id:
            return True
        else:
            return False


    def compare_public_address(self, instance_info, test_data) -> bool:
        """Compare the public address"""
        expected_address = instance_info['instance_public_address']
        actual_address = test_data['instance_public_address']
        if expected_address == actual_address:
            return True
        else:
            return False


    def compare_instance_state(self, instance_info, test_data) -> bool:
        """Compare the state"""
        expected_state = instance_info['instance_state']
        actual_state = test_data['instance_state']
        if expected_state == actual_state:
            return True
        else:
            return False


    def compare_security_groups(self, instance_info, test_data) -> bool:
        """Compare the security groups"""
        try:
            result = False
            expected_groups = instance_info['instance_securtity_groups']
            actual_groups = test_data['instance_securtity_groups']
            if expected_groups == actual_groups:
                result = True

            return result

        except Exception as e:
            print(e) 