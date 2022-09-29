from errno import ESOCKTNOSUPPORT
import pulumi
import pulumi_aws as eks


cluster = eks.Cluster("eks-cluster")

pulumi.export("kubeconfig", cluster.kubeconfig)
