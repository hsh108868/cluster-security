"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('pod_list')

# Export the name of the bucket
pulumi.export('pod_list', bucket.id)
