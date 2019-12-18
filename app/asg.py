import boto3
import sys
import logging
logging.basicConfig(level=logging.INFO)

asg_name=sys.argv[1]
logging.info("rolling asg: "+ asg_name)

asg_client = boto3.client('autoscaling') 
response = asg_client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[
        asg_name,
    ],
)

asgs = response["AutoScalingGroups"][0]
instances = asgs["Instances"]
ec2 = boto3.client('ec2')
waiter = ec2.get_waiter('instance_terminated')

for instance in instances:
    instance_id = instance["InstanceId"]
    logging.info("terminating instance: " + instance_id)
    ec2.terminate_instances(instance_ids=instance_id)
    waiter.wait(InstanceIds=[instance_id])