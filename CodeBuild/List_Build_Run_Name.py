import boto3

codebuild = boto3.client('codebuild')

response = codebuild.list_builds_for_project(
    projectName='developer-labs'
)
names = response["ids"]
for name in names:   #we can't use id because is key work so we use name varianle instead
    print(name)
    
    