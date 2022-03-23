"""
This test check the ec2 instance volume information and returns the fail or pass

"""

def test_check_ec2_instance_tags(get_volume_information, read_yaml, volume_object):
    """ Check the ec2 instance """
    try:
        expected_pass = 3
        actual_pass = 0
        # Compare volume is
        volume_id = volume_object.compare_volume_id(get_volume_information[0], read_yaml['ec2volume'])
        if volume_id:
            actual_pass += 1
            print(f"Gathered and Expected volume id are matching")
        else:
            print(f"volume id  are not matching the test is failed")

        # Compare volume size
        volume_size = volume_object.compare_volume_size(get_volume_information[0], read_yaml['ec2volume'])
        if volume_size:
            actual_pass += 1
            print(f"Gathered and Expected volume sizes are matching")
        else:
            print(f"volume sizes  are not matching the test is failed")

        # Compare volume state
        volume_state = volume_object.compare_volume_state(get_volume_information[0], read_yaml['ec2volume'])
        if volume_state:
            actual_pass += 1
            print(f"Gathered and Expected volume state are matching")
        else:
            print(f"volume states  are not matching the test is failed")

       

    except Exception as e:
        print(e)
        print("Error in the file")

    assert expected_pass == actual_pass,"Test failed: %s"%__file__



if __name__  == "__main__":

    test_result = test_check_ec2_instance_tags()
