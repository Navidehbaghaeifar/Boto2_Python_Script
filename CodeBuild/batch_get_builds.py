import boto3

codebuild = boto3.client('codebuild')

response = codebuild.batch_get_builds(
    ids=[
        'developer-labs:9762b47f-970f-4d20-8155-bebe3d74f562',
    ]
)
print(response)
