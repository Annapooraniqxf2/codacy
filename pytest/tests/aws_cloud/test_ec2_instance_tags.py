"""
This test check the ec2 instance information and returns the fail or pass

"""


def test_check_ec2_instance_tags(get_instance_information, read_yaml, ec2_object) -> None:
    """ Check the ec2 instance """
    try:
        expected_pass = 5
        actual_pass = 0
        # Compare ec2 tags
        tag_result = ec2_object.compare_ec2_tags(get_instance_information[0], read_yaml['ec2tags'])
        if tag_result:
            actual_pass += 1
            print(f"Gathered and Expected tags are matching")
        else:
            print(f"Tags are not matching the test is failed")

        # Compare image id
        image_result = ec2_object.compare_image_id(get_instance_information[0], read_yaml['ec2tags'])
        if image_result:
            actual_pass += 1
            print(f"Gathered image id and expected image id are matching")
        else:
            print(f"Image id are not matching the test is failed")

        # Compare instance public address
        public_address_result = ec2_object.compare_public_address(get_instance_information[0], read_yaml['ec2tags'])
        if public_address_result:
            actual_pass += 1
            print(f"Gathered and expected public address are matching")
        else:
            print(f"Public address are not matching the test is failed")

        # Compare instance state
        instance_state = ec2_object.compare_instance_state(get_instance_information[0], read_yaml['ec2tags'])
        if instance_state:
            actual_pass += 1
            print(f"Gathered and expected instance state are matching")
        else:
            print(f"Instance state are not matching the test is failed")


        # Compare Security groups
        instance_groups = ec2_object.compare_security_groups(get_instance_information[0], read_yaml['ec2tags'])
        if instance_groups:
            actual_pass += 1
            print(f"Gathered and expected instance groups are matching")
        else:
            print(f"Security groups are not matching the test is failed")

        

    except Exception as e:
        print(e)
        print("Error in the file")

    assert expected_pass == actual_pass,"Test failed: %s"%__file__



if __name__  == "__main__":
    test_check_ec2_instance_tags()