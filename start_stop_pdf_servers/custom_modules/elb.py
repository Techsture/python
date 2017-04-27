import boto3

def check_instance_health(conn, region, elb_name):
    response = conn.describe_instance_health(LoadBalancerName=elb_name)
    return response

def get_elb_connection(region):
    conn = boto3.client('elb', region_name=region)
    return conn

def describe_elb(conn, elb_name):
    status = conn.describe_load_balancers(LoadBalancerNames=[elb_name,])
    return status

def get_elb_sg_name(conn, elb_name):
    status = describe_elb(conn, elb_name)
    return status['LoadBalancerDescriptions'][0]['SourceSecurityGroup']['GroupName']

def add_instances_to_elb(conn, elb_name, instance_ids):
    # A list containing the dictionary is required for this boto function... hence the weirdness below of
    # converting the list to a list containing a dictionary:
    instance_dict = {}
    for instance in instance_ids:
        instance_dict_list = []
        instance_dict['InstanceId'] = instance
        instance_dict_list.append(instance_dict)
        # Needed to do this in the loop because it seems to only be processing the first item in the list:
        response = conn.register_instances_with_load_balancer(LoadBalancerName=elb_name, Instances=instance_dict_list)
    return response

def remove_instances_from_elb(conn, elb_name, instance_ids):
    # A list containing the dictionary is required for this boto function... hence the weirdness below of
    # converting the list to a list containing a dictionary:
    instance_dict = {}
    for instance in instance_ids:
        instance_dict_list = []
        instance_dict['InstanceId'] = instance
        instance_dict_list.append(instance_dict)
        # Needed to do this in the loop because it seems to only be processing the first item in the list:
        response = conn.deregister_instances_from_load_balancer(LoadBalancerName=elb_name, Instances=instance_dict_list)
    return response