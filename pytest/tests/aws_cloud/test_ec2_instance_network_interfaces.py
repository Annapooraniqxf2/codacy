"""
This test check the ec2 instance network information and returns the fail or pass

"""

def test_check_ec2_instance_network(get_network_information, read_yaml, network_object) -> None:
    """ Check the ec2 instance network info """
    try:
        expected_pass = 2
        actual_pass = 0
        # Compare volume is
        ip_address = network_object.compare_network_address(get_network_information, read_yaml['ec2network'])
        if ip_address:
            actual_pass += 1
            print(f"Gathered and Expected network ip addresses are matching")
        else:
            print(f"IP addresses  are not matching the test is failed")

        network_tag = network_object.compare_network_tag(get_network_information, read_yaml['ec2network'])
        if network_tag:
            actual_pass += 1
            print("Gathered and expected network tag names are mathcing")
        else:
            print("Network tag names are not matching and test is failed")        
       

    except Exception as e:
        print(e)
        print("Error in the file")

    assert expected_pass == actual_pass,"Test failed: %s"%__file__



if __name__  == "__main__":
    test_result = test_check_ec2_instance_network()
