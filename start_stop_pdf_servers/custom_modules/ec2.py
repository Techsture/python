import boto3
import sys

""" Global Vars used by all funcs """
regions = ["us-east-1", "us-west-1", "us-west-2"]
vpc_ids = { 'us-east-1' : 'vpc-9a80e1fe', 'us-west-1' : 'vpc-a66ce6c3', 'us-west-2' : 'vpc-53a69f36' }

def get_ec2_connection(region):
    conn = boto3.client('ec2', region_name=region)
    return conn

def get_sg_connection(region):
    sg_conn = boto3.resource('ec2', region_name=region)
    return sg_conn

def get_all_security_groups(conn, region="all"):
    """ takes a region and returns all security groups for that region.
        if no region is specified, return all regions security groups in list"""
    if region == "all":
        security_groups = []
        for reg in regions:
            security_groups.append(conn.describe_security_groups())
        return security_groups
    else:
        security_groups = conn.describe_security_groups()
        return security_groups

def find_security_group_by_name(conn, sg_name):
    """ Finds and returns a security group by name """
    sgs = conn.describe_security_groups(Filters=[{'Name': 'group-name', 'Values': [sg_name]}])
    return sgs

def create_security_group(conn, region, sg_name):
    """ Create a security group with name sg_name  """
    sg = conn.create_security_group(GroupName=sg_name, Description=sg_name, VpcId=vpc_ids[region])
    return sg

def get_security_group_obj(conn, region, sg_name):
    """ Takes a security group name and returns its ec2 object """
    sg_info = find_security_group_by_name(conn, sg_name)
    sgid = sg_info['SecurityGroups'][0]['GroupId']
    sg_conn = get_sg_connection(region)
    sg_obj = sg_conn.SecurityGroup(sgid)
    return sg_obj

def add_sg_name_tag(conn, region, sg_name, tag_value):
    """ takes a security group name and a tag value, creates a Name tag """
    sg = get_security_group_obj(conn, region, sg_name)
    tag = sg.create_tags(Tags=[{'Key':'Name','Value':tag_value}])
    return tag

def add_sg_ingress_cidr(conn, region, sg_name, port, cidr):
    """ takes a security group name, port, and ip(cidr) and adds ingress permissions """
    sg = get_security_group_obj(conn, region, sg_name)
    sg.authorize_ingress(IpProtocol="tcp",CidrIp=cidr,FromPort=port,ToPort=port)

def add_sg_ingress_sgname(conn, region, sg_name, ingress_sg_name, port):
    """ takes a security group name, security group name for ingress and port, adds ingress permissions """
    sg = get_security_group_obj(conn, region, sg_name)
    sg_ingress = get_security_group_obj(conn, region, ingress_sg_name)
    sg_response = sg.authorize_ingress(GroupId = sg.group_id, IpPermissions = [ {'IpProtocol': 'tcp', 'FromPort': port, 'ToPort': port, 'UserIdGroupPairs': [{ 'GroupId': sg_ingress.group_id}]}])

def get_all_reservations_for_region(conn, region):
    """ Get all ec2 reservations for a given region """
    reservations = conn.get_all_reservations()
    return reservations

def get_filtered_reservations_for_region(conn, region, ids):
    """ takes a region and list of instance ids, returns the associated ec2 object"""
    reservations = conn.get_all_reservations(instance_ids=ids)
    instances = []
    for r in reservations:
        instances.append(r.instances)
    return [i for sublist in instances for i in sublist]

def get_all_instances_for_region(conn, reservations):
    """ Given an boto ec2 reservation object, return all instances inside """
    instances = []
    for r in reservations:
        instances.append(r.instances)
    return instances

def get_instances_by_tag_name(conn, region, tag_name):
    """ Given a region and a tag value for the Name tag, return all instances.
    if wildcard is included, find those as well.
    """
    filtered = []
    if '*' in tag_name:
        stack = tag_name.replace('*','')
        #u'State': {u'Code': 16, u'Name': 'running'}, u
        reservations = conn.describe_instances(Filters=[{'Name':'tag-value', 'Values': [tag_name]}, { 'Name':'instance-state-code', 'Values':['16']}])
        #reservations = conn.describe_instances(Filters=[{'Name':'tag-value', 'Values': [tag_name]}])
        instances = [i for r in reservations['Reservations'] for i in r['Instances'] if 'Tags' in i]

    else:
        reservations = conn.describe_instances(Filters=[{'Name':'tag:Name', 'Values': [tag_name]}])
        #print reservations
        #reservations = conn.get_all_instances(filters={'tag:Name':tag_name, 'instance-state-name' : 'running'})
        instances = [i for r in reservations['Reservations'] for i in r['Instances']]
    return instances

def get_public_dns_by_tag_name(conn, region, tag_name):
    """ Given a region and a tag value for the Name tag, return all public DNS entries.
    If wildcard is included, find those as well. """
    instance_info = get_instances_by_tag_name(conn, region, tag_name)
    public_dns = []
    for i in instance_info:
        public_dns.append(i['PublicDnsName'])
    return public_dns

def get_public_dns_by_instance_id(conn, region, instance_ids):
    all_instances = conn.describe_instances()
    public_dns = []
    for reservation in all_instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['InstanceId'] in instance_ids:
                public_dns.append(instance['PublicDnsName'])
    return public_dns

def get_all_running_instances_for_region(conn, region, state, extra_args):
    """ Return all running instances in all regions """
    reservations = get_all_reservations_for_region(region)
    instances = get_all_instances_for_region(reservations)
    result = []
    for i in instances:
        if i[0].state == state and str(i[0].id) in extra_args:
            result.append(i)
    return result

def snapshot_volume(conn, region, volume_id, snapshot_name):
    """ takes a volumeid and tagname ( name you want to call the snapshot ) and performs an ebs snapshot """
    response = conn.create_snapshot(VolumeId=volume_id, Description=snapshot_name)
    return response

def list_snapshots_by_name_date(conn, region, snapshot_date):
    #response = conn.describe_snapshots( Filters=[ { 'Name': 'description', 'Values': [ snapshot_name, ] }, ] )
    response = conn.describe_snapshots()
    return response

def list_snapshots_by_name(conn, region, snapshot_name):
    response = conn.describe_snapshots( Filters=[ { 'Name': 'description', 'Values': [ snapshot_name, ] }, ] )
    #response = conn.describe_snapshots()
    return response

def delete_snapshot_by_id(conn, region, snapshot_id):
    response = conn.delete_snapshot(SnapshotId=snapshot_id)
    #response = conn.describe_snapshots()
    return response

def validate_region(region):
    """ Given a region, return true if in region list, otherwise return false"""
    if region.strip() in regions:
        return True
    else:
        return False

def start_instances(conn, instance_ids):
    response = conn.start_instances(InstanceIds=instance_ids)
    return response

def stop_instances(conn, instance_ids):
    response = conn.stop_instances(InstanceIds=instance_ids)
    return response