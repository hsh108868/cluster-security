from errno import ESOCKTNOSUPPORT
import pulumi
import pulumi_aws as eks
import pulumi_kubernetes as k8s


cluster = eks.Cluster("eks-cluster", eks.ClusterArgs(
    desired_capacity=2
))


node_group = eks.NodeGroup('eks-cluster-group',
                           cluster=cluster.core,
                           instance_type='t2.micro',
                           desired_capacity=1
                           )

pulumi.export("kubeconfig", cluster.kubeconfig)
