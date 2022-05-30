echo "kubectl installing"
sudo curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

if [["${?}" -ne 0]]; then
    echo "kubectl install failed"
    exit 1
fi
echo "success"

sudo chmod +x /usr/local/bin/kubectl
kubectl
