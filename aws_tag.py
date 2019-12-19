import boto3
import logging
import json

filename = 'test.json'


def getInstances(ec2):
    instances = ec2.instances
    #Return all AWS instances in the current environment
    return (instances)

def readJason(json_filename):
    with open(json_filename) as json_file:
        data = json.load(json_file)
    #return a JSON array of vaules from a file
    print(data)
    return (data)

def compareArrays(instances, tags):
    for ec2_instance in instances.all():
        print(ec2_instance)
        for tag in ec2_instance.tags:
            print(tag)
    #Return EC2 Instances that do not match any accept tag
    return ()
 
def lambda_handler(event, context):
    
    #Configure logging
    logger = logging.getLogger()
    logLevel  = logging.INFO

    #Create our EC2 client
    ec2 = boto3.resource('ec2')
    compareArrays(getInstances(ec2), readJason(filename))
    return

if __name__ == "__main__":
    event = []
    context = []
    lambda_handler(event, context)