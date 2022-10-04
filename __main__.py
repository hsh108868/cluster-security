"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3
import cluster.create_cluster as cluster
import Image_Vulnerability.docker as docker

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('pod-list')

# Export the name of the bucket
pulumi.export('pod-list', bucket.id)
cluster.create_cluster()
docker.docker()
