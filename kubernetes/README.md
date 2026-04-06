# SRE Challenge 


This project demonstrates running a simple Python Flask application in Kubernetes in an Alpine Linux Container on a local kubernetes cluster using Kind and Podman.

## Prerequisites
* Install kind: https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries
* Install Podman:  
```bash
sudo dnf -y install podman
```

> Note, this setup uses root based Podman and Kind. All kubectl commands must be ran with sudo as the root user has the kubeconfig for the kind cluster.

> For rootless Podman see the Github page: https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md

## Create the Kind cluster and sre-namespace
* To create the Kind cluster run the following command:
```bash
kind create cluster --name sre-challenge --config kubernetes/kind-config.yaml
```

## Building the container image
* Run the following commands to build the container image based on the Dockerfile:
```bash
podman build -f kubernetes/Dockerfile -t sre-challenge:local .
podman save sre-challenge:local -o sre-challenge.tar
sudo kind load image-archive sre-challenge.tar --name sre-challenge # Note, the actual image tag used in the manifest is localhost/sre-challenge:local
```
## Deploying the app
* First, add the Base64 encoded secret key to the file `kubernetes/manifests/sre-challenge-secret.yaml`. You can get the Base64 string with the following command:
```bash
echo -n "supersecretkey" | base64
```
* Apply the manifests for the secret and the app components themselves (deployment + service)
```bash
sudo kubectl apply -f kubernetes/manifests
```

* Acces the webapp by running this command and afterwards access the browser on http://localhost:5000
```bash
sudo kubectl port-forward svc/sre-challenge-svc 5000:5000 -n sre-challenge
```
