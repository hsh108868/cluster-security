import boto3


def describe_cluster(cluster_name):
    eks = boto3.client('eks', region_name='ap-northeast-2')
    print("EKS :", eks)
    try:
        response = eks.describe_cluster(name=cluster_name)
    except Exception as e:
        return None
    return response['cluster']  # eks


def main():
    test_cluster_name: 'Cluster-Security'
    result = describe_cluster(test_cluster_name)
    if result is None:
        print('Can`t gain about cluster information {}'.format(test_cluster_name))
    else:
        print('Cluster name'.format(result['name']))
        print('Status'.format(result['status']))


if __name__ == '__main__':
    main()
