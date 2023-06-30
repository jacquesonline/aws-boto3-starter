import boto3
session = boto3.session.Session(profile_name='external')
iam_resource = session.resource('iam')
aws_roles = []
for role in iam_resource.roles.all():
    aws_roles.append(role.name)
print('\n'.join(aws_roles))