# BackendSignAI

### Install Kind on linux
#### For AMD64 / x86_64
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
#### For ARM64
[ $(uname -m) = aarch64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-arm64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

### Install Kind on Windows Powershell
curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.20.0/kind-windows-amd64
Move-Item .\kind-windows-amd64.exe c:\some-dir-in-your-PATH\kind.exe

### Create Kind cluster
kind create cluster

### Delete Kind cluster
kind delete cluster


## Skaffold
### Installing
#### For Linux x86_64 (amd64)
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64 && \
sudo install skaffold /usr/local/bin/

#### For Linux ARMv8 (arm64)
curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-arm64 && \
sudo install skaffold /usr/local/bin/

#### For windows with Chocolatey
choco install -y skaffold

To create manifest: 
skaffold init --generate-manifests=true

### To build docker image:
docker build -t signai .

### To run docker container
docker run -d --name signaicontainer -p 80:80 signai

### To see logs in the container
docker logs signaicontainer

###  To delete image container
docker stop signaicontainer
docker rm signaicontainer