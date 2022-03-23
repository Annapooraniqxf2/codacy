"""
This page checks the fetched ec2 network interface info against with test data

"""


class NetworkCheck:
    """Contains method to compare the ec2 network interface date"""

    def compare_network_address(self, instance_info, test_data) -> bool:
        """Compare the ec2 network id"""
        result_flag = False
        expected_address = instance_info.private_ip_address
        actual_address = test_data['instance_ip_address']
        if expected_address == actual_address:
            result_flag = True

        return result_flag


    def compare_network_tag(self, instance_info, test_data) -> bool:
        """Compare the ec2 network tags"""
        result_flag = False
        expected_tag = instance_info.tag_set
        actual_tag = test_data['instance_tag']
        if expected_tag == actual_tag:
            result_flag = True

        return result_flag        