from errno import ESOCKTNOSUPPORT
import pulumi
import pulumi_aws as eks
import pulumi_kubernetes as k8s


cluster = eks.Cluster("eks-cluster")

pulumi.export("kubeconfig", cluster.kubeconfig)
