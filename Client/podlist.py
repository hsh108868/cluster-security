from urllib import response
from kubernetes import client, config
import boto3
import json

config.load_kube_config()

v1 = client.CoreV1Api()
pod_list = []

s3 = boto3.client('s3', region_name='ap-northwest-2')
response = s3.list_buckets()

buckets = [bucket['Name'] for bucket in response['Buckets']]
print(buckets)

print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:  # json 형태로 저장하기
    jsonString = json.dumps({"namespace :": i.metadata.namespace,
                            "pod_ip :": i.status.pod_ip, "pod_name :": i.metadata.name})
    pod_list.append(jsonString)

print(pod_list)
