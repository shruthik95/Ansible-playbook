
from __future__ import print_function
import argparse
import boto3
import sys
ec2 = boto3.client('ec2')
def parse_arguments(arguments):
      # type: (List) -> argparse.Namespace
      """
      Create the arguments parser
      """
      parser = argparse.ArgumentParser(description='Artifactory stats daemon')
      parser.add_argument('--verbose','-v', action='count')
      parser.add_argument('--keypair', type=str, help='Key pair name')
      parser.add_argument('--create', action='store_true', help='create instance')
      parser.add_argument('--start', help='Start instance')
      parser.add_argument('--stop', help='Stop instance')
      parser.add_argument('--terminate', type=str, help='Terminate instance')
      return parser.parse_args(arguments)

if __name__ == "__main__":
    args = parse_arguments(sys.argv[1:])
    print(args)
    
  if args.create:
         ec2 = boto3.resource('ec2', region_name='us-west-2')
         vpc = ec2.Vpc('vpc-2f022956')
         instance = ec2.create_instances(
                       ImageId='ami-0a11634d9ef4f142f',
                       MinCount=1,
                       MaxCount=1,
                       KeyName=args.keypair,
                       NetworkInterfaces=[{
                                "DeviceIndex":0,
                                "SubnetId":"subnet-e609bcad",
                                "Groups": ["sg-5389da22"],
                                 "AssociatePublicIpAddress":True}]
                       )
         print(instance[0].id)
         print("instance launched successfully")
  if args.start :
      print(args.start)
      print("instance running")
      try:
          ec2.start_instances(InstanceIds=[args.start])
      except Exception as e2:
         error2 = "Error2: %s" % str(e2)
         print(error2)
         sys.exit(0)
  if args.stop :
      print(args.stop)
      print("stopping the instance")
      try:
          ec2.stop_instances(InstanceIds=[args.stop])
      except Exception as e2:
          error2 = "Error2: %s" % str(e2)
          print(error2)
          sys.exit(0)
  if args.terminate :
      print(args.terminate)
      print("terminating the instance")
      try:
          ec2.terminate_instances(InstanceIds=[args.terminate])
      except Exception as e2:
          error2 = "Error2: %s" % str(e2)
          print(error2)
          sys.exit(0)
  