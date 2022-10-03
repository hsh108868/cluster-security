import pulumi
import pulumi_eks as eks


def create_cluster():

    cluster = eks.Cluster("eks-cluster", eks.ClusterArgs(
        desired_capacity=2
    ))

    node_group = eks.NodeGroup('eks-cluster-group',
                               cluster=cluster.core,
                               instance_type='t2.micro',
                               desired_capacity=1
                               )

    pulumi.export('eks-cluster', cluster.kubeconfig)
