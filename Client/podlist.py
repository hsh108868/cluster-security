import pulumi
from pulumi_aws import s3

bucket = s3.Bucket('pod_list')

pulumi.export('pod_list', bucket.id)
